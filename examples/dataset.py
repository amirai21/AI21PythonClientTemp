from ai21.ai21_studio_client import AI21StudioClient
from ai21.data_types import ClientConfigs

api_key = "Pb8tSv5x7kyxeOuHSEMVhpUU18kyordA"
configs = ClientConfigs(num_retries=0)
client = AI21StudioClient(api_key, configs)
response = client.dataset.upload_dataset(
        file_path='/Users/amirkoblyansky/workspace/studio-datasets/tests/test_files/valid.jsonl', dataset_name='my_new_ds13', delete_long_rows=True)

print(response)
