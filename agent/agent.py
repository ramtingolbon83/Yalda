import json

from model.client import ModelClient
from tools.registry import tool_registry


class Agent:
    def __init__(self):
        self.model = ModelClient()

    def chat(self, messages, tools):
        while True:
            result = self.model.chat(messages, tools)
            message = result["choices"][0]["message"]

            if "tool_calls" not in message:
                return result
            messages.append(message)
            for tool_call in message["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                arguments = tool_call["function"]["arguments"]
                arguments = json.loads(arguments)
                tool = tool_registry[tool_name]
                tool_result = tool(**arguments)

                tool_answer = {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": str(tool_result),
                }

                messages.append(tool_answer)
