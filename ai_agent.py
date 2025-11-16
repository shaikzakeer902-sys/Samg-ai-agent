import openai

class AIAgent:
    def __init__(self, api_key, system_prompt="You are a helpful AI agent."):
        openai.api_key = api_key
        self.system_prompt = system_prompt

    def query(self, user_message):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_tokens=300,
        )
        return response['choices'][0]['message']['content']

if __name__ == "__main__":
    agent = AIAgent(api_key="YOUR_OPENAI_API_KEY")
    print("Hello! Type your questions below. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        answer = agent.query(user_input)
        print("Agent:", answer)