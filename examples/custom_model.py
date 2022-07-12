from ai21.ai21_studio_client import AI21StudioClient
from ai21.data_types import ClientConfigs


def get_custom_models():
    api_key = "Pb8tSv5x7kyxeOuHSEMVhpUU18kyordA"
    configs = ClientConfigs(num_retries=0)
    client = AI21StudioClient(api_key, configs)
    response = client.custom_model.get_custom_models()
    print(response)


if __name__ == "__main__":
    get_custom_models()