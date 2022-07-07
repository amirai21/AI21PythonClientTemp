from src.ai21.constants import DEFAULT_API_VERSION, STUDIO_HOST
from src.ai21.http_client import HttpClient
from src.ai21.errors import InputValidationException


class Tokenize:

    def __init__(self, http_client: HttpClient, api_version: str = DEFAULT_API_VERSION):
        self.api_version = api_version
        self.http_client = http_client
        self.base_url = f'{STUDIO_HOST}/studio/{api_version}'

    def tokenize(self, **params):
        text = params.get('text', None)
        if text is None:
            raise InputValidationException('text is required for the tokenize request')
        return self.http_client.execute_http_request(method='POST', url=f'{self.base_url}/tokenize', **params)



