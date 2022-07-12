from typing import Optional

from ai21 import api_key_global
from ai21.constants import DEFAULT_API_VERSION, STUDIO_HOST
from ai21.data_types import ClientConfigs
from ai21.errors import InputValidationException
from ai21.http_client import HttpClient
from ai21.modules.completion import Completion
from ai21.modules.custom_model import CustomModel
from ai21.modules.dataset import Dataset
from ai21.modules.tokenize import Tokenize
from ai21.version import __version__
SUPPORTED_API_VERSIONS = ['v1']


class AI21StudioClient:
    def __init__(self, api_key: str, configs: Optional[ClientConfigs] = None, **params):
        print(f'api_key_global: {api_key_global}')
        self.api_key = api_key
        api_version = params.get('api_version', None)
        if api_version is not None and api_version not in SUPPORTED_API_VERSIONS:
            raise InputValidationException(f'Supplied api_version is not supported. Supported versions are: ' + ','.join(SUPPORTED_API_VERSIONS))
        if api_version is None:
            api_version = DEFAULT_API_VERSION
        self.api_version = api_version
        application = params.get('application', None)
        if application is not None:
            self.application = application
        default_headers = self.build_default_headers()
        if not configs:
            configs = ClientConfigs()
        if not configs.headers:
            configs.headers = {}
        configs.headers.update(default_headers)
        http_client = HttpClient(configs)
        api_host = configs.api_host if configs.api_host is not None else STUDIO_HOST
        # Initializing API modules:
        self.completion = Completion(http_client, api_version, api_host)
        self.custom_model = CustomModel(http_client, api_version, api_host)
        self.dataset = Dataset(http_client, api_version, api_host)
        self.tokenize = Tokenize(http_client, api_version, api_host)

    def build_user_agent(self):
        return f'AI21 Studio {self.api_version} API Client version {__version__}'

    def build_default_headers(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': self.build_user_agent()
        }
        return headers

