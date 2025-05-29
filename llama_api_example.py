import json
import os
import requests

# TODO set your Llama API key as an environment variable
LLAMA_API_KEY = os.environ.get("LLAMA_API_KEY")

# Define the API endpoint URL
url = "https://api.llama.com/v1/chat/completions"

# Define the headers
headers = {
    "Authorization": f"Bearer {LLAMA_API_KEY}",
    "Content-Type": "application/json"
}

# Define the data
data = {
    "model": "Llama-4-Maverick-17B-128E-Instruct-FP8",
    "messages": [
        {
            "role": "system",
            "content": "You are a friendly and knowledgeable assistant. You have access to a vast amount of information and can provide helpful responses to a wide range of questions and topics. Your goal is to assist users with their queries, providing accurate and relevant information in a clear and concise manner. You should be able to understand the context of the user's request and respond accordingly. Please keep your responses brief and to the point, avoiding unnecessary details or tangents. If you're unsure or don't know the answer to a question, please say so and try to provide alternative sources or suggestions. Remember to always maintain a professional and respectful tone, avoiding any language or content that may be considered offensive or inappropriate."
        },
        {
            "role": "user",
            "content": "Hello, world! What can you do for me today?"
        }
    ]
}

# Convert the data to JSON
json_data = json.dumps(data)
# Send the POST request
response = requests.post(url, headers=headers, data=json_data)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
