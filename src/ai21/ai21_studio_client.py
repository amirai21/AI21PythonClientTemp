from typing import Optional
from data_types import ClientConfigs
from http_client import HttpClient
from src.ai21.constants import DEFAULT_API_VERSION
from src.ai21.errors import InputValidationException
from src.ai21.modules.completion import Completion
from src.ai21.modules.custom_model import CustomModel
from src.ai21.modules.dataset import Dataset
from src.ai21.version import __version__
SUPPORTED_API_VERSIONS = ['v1']


class AI21StudioClient:
    def __init__(self, api_key: str, configs: Optional[ClientConfigs] = None, **params):
        self.api_key = api_key
        api_version = params.get('api_version', None)
        if api_version is not None and api_version not in SUPPORTED_API_VERSIONS:
            raise InputValidationException(f'Supplied api_version is not supported. Supported versions are: ' + ','.join(SUPPORTED_API_VERSIONS))
        if api_version is None:
            api_version = DEFAULT_API_VERSION
        self.api_version = api_version
        user_pid = params.get('user_id', None)
        if user_pid is not None:
            self.user_pid = user_pid
        app_name = params.get('app_name', None)
        if app_name is not None:
            self.app_name = app_name
        default_headers = self.build_default_headers()
        if not configs:
            configs = ClientConfigs()
        if not configs.headers:
            configs.headers = {}
        configs.headers.update(default_headers)
        http_client = HttpClient(configs)
        # Initializing all supported API modules:
        self.completion = Completion(http_client, api_version)
        self.custom_model = CustomModel(http_client, api_version)
        self.dataset = Dataset(http_client, api_version)

    def build_user_agent(self):
        return f'AI21 Studio {self.api_version} API Client version {__version__}'

    def build_default_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': self.build_user_agent()
        }
