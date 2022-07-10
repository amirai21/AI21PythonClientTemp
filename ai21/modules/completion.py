from typing import Dict

from ai21.data_types import Penalty
from ai21.http_client import HttpClient
from ai21.errors import InputValidationException
from ai21.utils import to_dict, build_ai21studio_response

COMPLETION_MODULE_NAME = 'complete'


def validate_input(params: Dict):
    prompt = params.get('prompt', None)
    if prompt is None:
        raise InputValidationException('prompt is required for the completion request')
    if not isinstance(prompt, str):
        raise InputValidationException(f'The prompt supplied in the request input is a ${type(prompt)} instead of a string')
    if params.get('stopSequences', None) is None:
        params['stopSequences'] = []
    if params.get('countPenalty', None) is None:
        params['countPenalty'] = to_dict(Penalty(scale=0))
    if params.get('frequencyPenalty', None) is None:
        params['frequencyPenalty'] = to_dict(Penalty(scale=0))
    if params.get('presencePenalty', None) is None:
        params['presencePenalty'] = to_dict(Penalty(scale=0))


class Completion:

    def __init__(self, http_client: HttpClient, api_version: str, api_host: str):
        self.api_version = api_version
        self.http_client = http_client
        self.base_url = f'{api_host}/studio/{api_version}'

    @build_ai21studio_response
    def complete(self, model_name: str, **params):
        validate_input(**params)
        return self.http_client.execute_http_request(method='POST', url=f'{self.base_url}/{model_name}/complete', **params)



