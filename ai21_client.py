from typing import Optional, Dict

from data_types import ClientConfigs, CompletionParams
from http_client import HttpClient


class AI21Client:
    def __init__(self, api_key: str, configs: Optional[ClientConfigs] = None):
        default_headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
        if not configs:
            configs = ClientConfigs()
        if not configs.headers:
            configs.headers = {}
        configs.headers.update(default_headers)
        self.api_key = api_key
        self.http_client = HttpClient(configs)

    def completion(self, params: Dict):
        return self.http_client.execute_http_request('POST', 'https://api.ai21.com/studio/v1/j1-jumbo/complete', params)
