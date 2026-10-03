from agent.agent import Agent
from tools.schemas import tools

agent = Agent()
messages = []

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Good bye!")
        break
    messages.append({"role": "user", "content": user_message})

    result = agent.chat(messages, tools)
    answer = result["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": answer})
    print(f"AI: {answer}")
