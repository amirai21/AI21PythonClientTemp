
from ai21.http_client import HttpClient
from ai21.modules.studio_api_module import AI21StudioModule
from ai21.utils import build_ai21studio_response

DATASET_MODULE_NAME = 'dataset'


class Dataset(AI21StudioModule):

    def __init__(self, http_client: HttpClient, api_version: str, api_host: str):
        super().__init__(http_client, api_version, api_host)

    @build_ai21studio_response
    def get_datasets(self):
        return self.list(DATASET_MODULE_NAME)

    @build_ai21studio_response
    def get_dataset(self, dataset_pid: str):
        return self.get(DATASET_MODULE_NAME, dataset_pid)

    @build_ai21studio_response
    def upload_dataset(self, file_path: str, dataset_name: str, **params):
        files = {'dataset_file': open(file_path, 'rb')}
        params['dataset_name'] = dataset_name
        return self.create_with_files_upload(DATASET_MODULE_NAME, files, **params)

