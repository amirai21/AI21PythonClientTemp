import argparse

from ai21 import data_types, utils
from ai21.ai21_studio_client import AI21StudioClient

body = {
    "prompt": "The following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Male.\n\nConversation:\nUser: Hi, had a question\nMax: Hi there, happy to help!\nUser: Is there no way to return a product? I got your blue T-Shirt size small but it doesn't fit.\nMax: I'm sorry to hear that. Unfortunately we don't have a return policy. \nUser: That's a shame. \nMax: Is there anything else i can do for you?\n\n##\n\nThe following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, I was wondering when you'll have the \"Blue & White\" t-shirt back in stock?\nMax: Hi, happy to assist! We currently don't have it in stock. Do you want me to send you an email once we do?\nUser: Yes!\nMax: Awesome. What's your email?\nUser: anc@gmail.com\nMax: Great. I'll send you an email as soon as we get it.\n\n##\n\nThe following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, how much time does it take for the product to reach me?\nMax: Hi, happy to assist! It usually takes 5 working days to reach you.\nUser: Got it! thanks. Is there a way to shorten that delivery time if i pay extra?\nMax: I'm sorry, no.\nUser: Got it. How do i know if the White Crisp t-shirt will fit my size?\nMax: The size charts are available on the website.\nUser: Can you tell me what will fit a young women.\nMax: Sure. Can you share her exact size?\n\n##\n\nThe following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, I have a question for you",
    "numResults": 1,
    "maxTokens": 100,
    "temperature": 0.58,
    "topKReturn": 0,
    "topP": 1,
    "countPenalty": {
        "scale": 0.25,
        "applyToNumbers": False,
        "applyToPunctuations": False,
        "applyToStopwords": False,
        "applyToWhitespaces": False,
        "applyToEmojis": False
    },
    "frequencyPenalty": {
        "scale": 0,
        "applyToNumbers": False,
        "applyToPunctuations": False,
        "applyToStopwords": False,
        "applyToWhitespaces": False,
        "applyToEmojis": False
    },
    "presencePenalty": {
        "scale": 0,
        "applyToNumbers": False,
        "applyToPunctuations": False,
        "applyToStopwords": False,
        "applyToWhitespaces": False,
        "applyToEmojis": False
    },
    "stopSequences": ["##", "User:"]
}


def test_http_call(api_key: str):
    configs = data_types.ClientConfigs(num_retries=0)
    client = AI21StudioClient(api_key, configs)

    prompt = "The following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Male.\n\nConversation:\nUser: Hi, had a question\nMax: Hi there, happy to help!\nUser: Is there no way to return a product? I got your blue T-Shirt size small but it doesn't fit.\nMax: I'm sorry to hear that. Unfortunately we don't have a return policy. \nUser: That's a shame. \nMax: Is there anything else i can do for you?\n\n##\n\nThe following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, I was wondering when you'll have the \"Blue & White\" t-shirt back in stock?\nMax: Hi, happy to assist! We currently don't have it in stock. Do you want me to send you an email once we do?\nUser: Yes!\nMax: Awesome. What's your email?\nUser: anc@gmail.com\nMax: Great. I'll send you an email as soon as we get it.\n\n##\n\nThe following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, how much time does it take for the product to reach me?\nMax: Hi, happy to assist! It usually takes 5 working days to reach you.\nUser: Got it! thanks. Is there a way to shorten that delivery time if i pay extra?\nMax: I'm sorry, no.\nUser: Got it. How do i know if the White Crisp t-shirt will fit my size?\nMax: The size charts are available on the website.\nUser: Can you tell me what will fit a young women.\nMax: Sure. Can you share her exact size?\n\n##\n\nThe following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, I have a question for you"
    frequency_penalty = data_types.Penalty(scale=0.2)
    completion_params = data_types.CompletionParams(prompt=prompt, maxTokens=20, temperature=0.58, frequencyPenalty=frequency_penalty)
    response = client.completion.complete(model_name='j1-jumbo', params=utils.to_dict(completion_params))
    print(response)


parser = argparse.ArgumentParser()
parser.add_argument('--api_key', type=str, required=True)
args = parser.parse_args()
test_http_call(args.api_key)
