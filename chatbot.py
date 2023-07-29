import openai

openai.api_key = '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'

def chatbot_response(messages):
    user_input = messages[-1]["content"]

    if user_input.lower() == "bye":
        return "Goodbye! Have a great day."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]
