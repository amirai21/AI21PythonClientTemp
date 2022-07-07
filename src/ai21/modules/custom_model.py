from src.ai21.constants import DEFAULT_API_VERSION
from src.ai21.http_client import HttpClient
from src.ai21.modules.studio_api_module import AI21StudioModule
from src.ai21.utils import measure_execution_time

CUSTOM_MODEL_MODULE_NAME = 'custom-model'


class CustomModel(AI21StudioModule):

    def __init__(self, http_client: HttpClient, api_version: str = DEFAULT_API_VERSION):
        super().__init__(http_client, api_version)

    @measure_execution_time
    def get_custom_models(self):
        return self.list(CUSTOM_MODEL_MODULE_NAME)

    @measure_execution_time
    def get_custom_model(self, custom_model_pid: str):
        return self.get(CUSTOM_MODEL_MODULE_NAME, custom_model_pid)

    @measure_execution_time
    def train_custom_model(self, **params):
        return self.http_client.execute_http_request(method='POST', url=f'{self.base_url}/{CUSTOM_MODEL_MODULE_NAME}', **params)

