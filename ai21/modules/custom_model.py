from ai21.http_client import HttpClient
from ai21.modules.studio_api_module import AI21StudioModule
from ai21.utils import build_ai21studio_response

CUSTOM_MODEL_MODULE_NAME = 'custom-model'


class CustomModel(AI21StudioModule):

    def __init__(self, http_client: HttpClient, api_version: str, api_host: str):
        super().__init__(http_client, api_version, api_host)

    @build_ai21studio_response
    def get_custom_models(self):
        return self.list(CUSTOM_MODEL_MODULE_NAME)

    @build_ai21studio_response
    def get_custom_model(self, custom_model_pid: str):
        return self.get(CUSTOM_MODEL_MODULE_NAME, custom_model_pid)

    @build_ai21studio_response
    def train_custom_model(self, **params):
        return self.create(CUSTOM_MODEL_MODULE_NAME, params)

