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
