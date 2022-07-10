
from ai21.http_client import HttpClient
from ai21.errors import InputValidationException
from ai21.utils import build_ai21studio_response


def validate_input(params):
    text = params.get('text', None)
    if text is None:
        raise InputValidationException('text is required for the tokenize request')


class Tokenize:

    def __init__(self, http_client: HttpClient, api_version: str, api_host: str):
        self.api_version = api_version
        self.http_client = http_client
        self.base_url = f'{api_host}/studio/{api_version}'

    @build_ai21studio_response
    def tokenize(self, **params):
        validate_input(params)
        return self.http_client.execute_http_request(method='POST', url=f'{self.base_url}/tokenize', params=params)



