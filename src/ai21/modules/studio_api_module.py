from src.ai21.constants import STUDIO_HOST
from src.ai21.http_client import HttpClient


class AI21StudioModule:
    def __init__(self, http_client: HttpClient, api_version: str):
        self.api_version = api_version
        self.http_client = http_client
        self.base_url = f'{STUDIO_HOST}/studio/{api_version}'

    def list(self, module_name: str):
        return self.http_client.execute_http_request(method='GET', url=f'{self.base_url}/{module_name}')

    def get(self, module_name: str, pid: str):
        return self.http_client.execute_http_request(method='GET', url=f'{self.base_url}/{module_name}/{pid}')


