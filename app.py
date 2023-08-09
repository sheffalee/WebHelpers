import streamlit as st
import openai
from sentiment_analysis import get_sentiment_label

# Set up OpenAI API
openai.api_key = st.secrets['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']

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

def main():
    st.title("Web Helpers App")

    # Chatbot and Sentiment Analysis section
    
    # Sentiment Analysis section
    st.title("Sentiment Analysis")
    user_review = st.text_area("Enter your review here")

    if user_review:
        sentiment_label = get_sentiment_label(user_review)
        st.write("Sentiment:", sentiment_label)

    #chatbot section
    st.title("Chatbot")
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("Enter your queries here")

    if user_input:
        chatbot_response = generate_response(user_input)
        st.session_state.conversation.append(("user", user_input))
        st.session_state.conversation.append(("bot", chatbot_response))

    for role, text in st.session_state.conversation:
        if role == "user":
            st.text_input("You:", text, key=text)
        else:
            st.text_area("ChatBot:", text, key=text)

    st.write("------")

    

if __name__ == '__main__':
    main()

