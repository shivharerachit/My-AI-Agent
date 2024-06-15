import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
openai_api_key = os.environ["AZURE_OPENAI_API_KEY"]
deployment = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
# search_endpoint = os.environ["SEARCH_ENDPOINT"]
# search_index = os.environ["SEARCH_INDEX"]
      
      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=openai_api_key,
    api_version="2024-02-01",
)

prompt = [
        {
            "role": "system",
            "content": "You are a highly skilled AI assistant named 'Djamgo' created by 'RACHIT SHIVHARE' with expertise in programming. Your task is to understand and complete the provided code snippets. You should infer the missing parts based on the context and ensure the completed code is functional and follows best practices. After ensuring the code is correct remove the part entered by user and complete it by providing next line."
        },
        # {
        #     "role": "assistant",
        #     "content": "Waiting for the code snippet to complete..."
        # },
        {
            "role": "user",
            "content": "python\ndef calculate_sum(a, b):\n    return "
        },
        {
            "role": "assistant",
            "content": " a + b"
        },
        {
            "role": "user",
            "content": "function greet(name) {\n    console.log(\"Hello, \" + );\n}"
        },
        {
            "role": "assistant",
            "content": " name);\n}"
        },
        {
            "role": "user",
            "content": "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println();\n    }\n}"
        },
        {
            "role": "assistant",
            "content": "(\"Hello, World!\");\n    }\n}"
        },
        # {
        #     "role": "user",
        #     "content": "function startRocket() {var speedInput = document.getElementById('speedInput');var rocket = document.getElementById('rocket');var speed = parseInt(speedInput.value, 10) || 1;"
        # },
    ]
# completion = client.chat.completions.create(
# model=deployment,
# messages=prompt
# )

# print(completion.choices[0].message.content)
# print(completion.to_json())

def askGPT(askPrompt):
    prompt.append(
        {
            "role": "user",
            "content": askPrompt
        }
    )
    completion = client.chat.completions.create(
    model=deployment,
    messages=prompt
    )
    return completion.choices[0].message.content


























# extra_body={
#     "data_sources": [
#         {
#             "type": "azure_search",
#             "parameters": {
#                 "endpoint": search_endpoint,
#                 "index_name": search_index,
#                 "authentication": {
#                     "type": "system_assigned_managed_identity"
#                 }
#             }
#         }
#     ]
# }