import json
from typing import Optional, Dict

from data_types import ClientConfigs, CompletionParams, Penalty
from http_client import HttpClient
from src.ai21.errors import InputValidationException
from src.ai21.utils import to_dict


def validate_input(params):
    prompt = params.get('prompt', None)
    if prompt is None:
        raise InputValidationException('prompt is required as input for the completion request')
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

    def completion(self, **params):
        # validate_input(**params)
        return self.http_client.execute_http_request(
            method='POST', url='https://api.ai21.com/studio/v1/j1-jumbo/complete', **params)
