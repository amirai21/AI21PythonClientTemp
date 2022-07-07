from src.ai21.constants import DEFAULT_API_VERSION
from src.ai21.http_client import HttpClient
from src.ai21.modules.studio_api_module import AI21StudioModule
from src.ai21.utils import measure_execution_time

DATASET_MODULE_NAME = 'dataset'


class Dataset(AI21StudioModule):

    def __init__(self, http_client: HttpClient, api_version: str = DEFAULT_API_VERSION):
        super().__init__(http_client, api_version)

    @measure_execution_time
    def get_datasets(self):
        return self.list(DATASET_MODULE_NAME)

    @measure_execution_time
    def get_dataset(self, dataset_pid: str):
        return self.get(DATASET_MODULE_NAME, dataset_pid)

    @measure_execution_time
    def upload_dataset(self, file_path: str, dataset_name: str, **params):
        files = {'dataset_file': open(file_path, 'rb')}
        params['dataset_name'] = dataset_name
        return self.http_client.execute_http_request(method='POST', url=f'{self.base_url}/{DATASET_MODULE_NAME}', params=params, files=files)

