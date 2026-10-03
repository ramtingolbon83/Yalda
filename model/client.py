import requests

MODEL_URL = "http://127.0.0.1:8080/v1/chat/completions"


class ModelClient:
    def chat(self, messages, tools):
        data = {
            "messages": messages,
            "tools": tools,
            "temperature": 0.7,
            "max_tokens": 500,
        }
        response = requests.post(MODEL_URL, json=data)
        result = response.json()
        return result