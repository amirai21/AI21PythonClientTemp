import json
from typing import Optional, Dict
import requests
from requests.adapters import HTTPAdapter

from data_types import ClientConfigs

DEFAULT_TIMEOUT_SEC = 30
DEFAULT_NUM_RETRIES = 2


class AI21Client:
    def __init__(self, api_key: str, configs: Optional[ClientConfigs] = None):
        self.api_key = api_key
        self.timeout_sec = configs.timeout_sec if configs and configs.timeout_sec else DEFAULT_TIMEOUT_SEC
        self.num_retries = configs.num_retries if configs and configs.num_retries else DEFAULT_NUM_RETRIES
        self.headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

    def execute_http_request(
            self,
            method: str,
            url: str,
            params: Optional[Dict] = None,
            req_headers: Optional[Dict] = None,
            timeout_sec: Optional[int] = None,
            num_retries: Optional[int] = None):

        adapter = HTTPAdapter(max_retries=num_retries if num_retries else self.num_retries)
        session = requests.Session()
        session.mount("https://", adapter)
        timeout = timeout_sec if timeout_sec else self.timeout_sec
        headers = req_headers if req_headers else self.headers
        data = json.dumps(params).encode()
        response = session.request(method, url, headers=headers, data=data, timeout=timeout)
        return response
