from src.ai21.constants import DEFAULT_API_VERSION, STUDIO_HOST
from src.ai21.data_types import Penalty
from src.ai21.http_client import HttpClient
from src.ai21.modules.studio_api_module import AI21StudioModule
from src.ai21.errors import InputValidationException
from src.ai21.utils import to_dict, measure_execution_time

COMPLETION_MODULE_NAME = 'complete'


def validate_input(params):
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

    def __init__(self, http_client: HttpClient, api_version: str = DEFAULT_API_VERSION):
        self.api_version = api_version
        self.http_client = http_client
        self.base_url = f'{STUDIO_HOST}/studio/{api_version}'

    @measure_execution_time
    def complete(self, model_name: str, **params):
        validate_input(**params)
        return self.http_client.execute_http_request(method='POST', url=f'{self.base_url}/{model_name}/complete', **params)



