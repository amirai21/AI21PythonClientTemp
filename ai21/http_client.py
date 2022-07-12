import json
from typing import Optional, Dict
import requests
from requests.adapters import HTTPAdapter, Response, Retry, RetryError

from ai21.data_types import ClientConfigs
from ai21.errors import BadRequest, Unauthorized, UnprocessableEntity, TooManyRequests, ServerError, ServiceUnavailable, AI21HttpException

DEFAULT_TIMEOUT_SEC = 30
DEFAULT_NUM_RETRIES = 0
MAX_RETRY_FOR_SESSION = 2
RETRY_BACK_OFF_FACTOR = 0.3
TIME_BETWEEN_RETRIES = 1000
RETRY_ERROR_CODES = (429, 500, 503)
RETRY_METHOD_WHITELIST = ['GET', 'POST', 'PUT']


def handle_non_success_response(response: Response):
    if response.status_code == 400:
        raise BadRequest(details=response.text)
    if response.status_code == 401:
        raise Unauthorized(details=response.text)
    if response.status_code == 422:
        raise UnprocessableEntity(details=response.text)
    if response.status_code == 429:
        raise TooManyRequests(details=response.text)
    if response.status_code == 500:
        raise ServerError(details=response.text)
    if response.status_code == 503:
        raise ServiceUnavailable(details=response.text)
    raise AI21HttpException(response.status_code, details=response.text)


def requests_retry_session(session, retries=0):
    retry = Retry(total=retries, read=retries, connect=retries, backoff_factor=RETRY_BACK_OFF_FACTOR,
                  status_forcelist=RETRY_ERROR_CODES, method_whitelist=frozenset(RETRY_METHOD_WHITELIST))
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session


class HttpClient:
    def __init__(self, configs: Optional[ClientConfigs] = None):
        self.timeout_sec = configs.timeout_sec if configs and configs.timeout_sec else DEFAULT_TIMEOUT_SEC
        self.num_retries = configs.num_retries if configs and configs.num_retries else DEFAULT_NUM_RETRIES
        self.headers = configs.headers if configs and configs.headers else {}
        self.apply_retry_policy = self.num_retries > 0

    def execute_http_request(self, method: str, url: str, params: Optional[Dict] = None, files=None):
        session = requests_retry_session(requests.Session(), retries=self.num_retries) if self.apply_retry_policy else requests.Session()
        timeout = self.timeout_sec
        headers = self.headers
        data = json.dumps(params).encode()
        try:
            print(f'Calling {method} {url} {data}')
            if method == 'GET':
                response = session.request(method, url, headers=headers, timeout=timeout)
            elif files is not None:
                if method != 'POST':
                    raise Exception(f'execute_http_request supports only POST for files upload, but {method} was supplied instead')
                if 'Content-Type' in headers:
                    headers.pop('Content-Type')  # multipart/form-data 'Content-Type' will be added when passing rb files and payload
                response = session.request(method, url, headers=headers, data=params, files=files, timeout=timeout)
            else:
                response = session.request(method, url, headers=headers, data=data, timeout=timeout)
        except ConnectionError as connection_error:
            print(f'Calling {method} {url} failed with ConnectionError: {connection_error}')
            raise connection_error
        except RetryError as retry_error:
            print(f'Calling {method} {url} failed with RetryError: {retry_error}')
            raise retry_error
        except Exception as exception:
            print(f'Calling {method} {url} failed with Exception: {exception}')
            raise exception

        if response.status_code != 200:
            handle_non_success_response(response)

        return response.headers, response.json()
