import json
from typing import Optional, Dict
import requests
from requests.adapters import HTTPAdapter, Response

from data_types import ClientConfigs

DEFAULT_TIMEOUT_SEC = 30
DEFAULT_NUM_RETRIES = 2


class HttpClient:
    def __init__(self, configs: Optional[ClientConfigs] = None):
        self.timeout_sec = configs.timeout_sec if configs and configs.timeout_sec else DEFAULT_TIMEOUT_SEC
        self.num_retries = configs.num_retries if configs and configs.num_retries else DEFAULT_NUM_RETRIES
        self.headers = configs.headers if configs and configs.headers else {}

    def handle_non_success_response(self, response: Response):
        if response.status_code == 401:
            print('401')
            raise Exception('AI21 Unauthorized exception TBD')
        if response.status_code == 400:
            print('400')
            raise Exception('AI21 bad request exception TBD')
        if response.status_code == 429:
            print('429')
            raise Exception('AI21 rate limit exception TBD')
        # ...
        raise Exception('AI21 general http handle_non_success_response exception TBD')

    def execute_http_request(
            self,
            method: str,
            url: str,
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None,
            timeout_sec: Optional[int] = None,
            num_retries: Optional[int] = None):

        adapter = HTTPAdapter(max_retries=num_retries if num_retries else self.num_retries)
        session = requests.Session()
        session.mount("https://", adapter)
        timeout = timeout_sec if timeout_sec else self.timeout_sec
        headers = self.headers.update(headers) if headers else self.headers
        data = json.dumps(params).encode()
        try:
            response = session.request(method, url, headers=headers, data=data, timeout=timeout)
        except ConnectionError as connection_error:
            print(f'Calling {method} {url} failed with ConnectionError: {connection_error}')
            raise connection_error

        if response.status_code != 200:
            self.handle_non_success_response(response)

        return response.json()
