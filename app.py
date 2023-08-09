import streamlit as st
import openai
from sentiment_analysis import get_sentiment_label

# Set up OpenAI API
openai.api_key = st.secrets["api_secret"]

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

    user_input = st.text_input("ChatBot: Enter your queries here")

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

# import streamlit as st
# import openai
# from streamlit_chat import message
# from sentiment_analysis import get_sentiment_label

# # Set up OpenAI API
# openai.api_key = st.secrets["api_secret"]

# def generate_response(prompt):
#     completions = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     message = completions.choices[0].text
#     return message

# def main():
#     st.title("ChatBot and Sentiment Analysis")

#     # Chatbot section
#     if 'past' not in st.session_state:
#         st.session_state['past'] = []
#     if 'generated' not in st.session_state:
#         st.session_state['generated'] = []

#     user_input = st.text_input("ChatBot: Enter your queries here")

#     if user_input:
#         chatbot_response = generate_response(user_input)
#         st.session_state.generated.append(chatbot_response)
#         st.session_state.past.append(user_input)

#     if st.session_state['generated']:
#         for i in range(len(st.session_state['generated']) - 1, -1, -1):
#             message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
#             message(st.session_state["generated"][i], key=str(i))

#     st.write("------")

#     # Sentiment Analysis section
#     st.title("Sentiment Analysis")
#     user_review = st.text_area("Enter your review here")

#     if user_review:
#         sentiment_label = get_sentiment_label(user_review)
#         st.write("Sentiment:", sentiment_label)

# if __name__ == '__main__':
#     main()

# # import streamlit as st
# # import pickle
# # from sentiment_analysis import get_sentiment_label 
# # import openai
# # import streamlit as st
# # from streamlit_chat import message

# # def main():
# #     # Set a title for the app
# #     st.title("Sentiment Analysis Web App")

# #     # Get input text from the user
# #     user_input = st.text_area("Enter your review here:")
    
# #     # Check if the user has entered any text
# #     if user_input:
# #         # Perform sentiment analysis and get the sentiment label
# #         sentiment_label = get_sentiment_label(user_input)

# #         # Display the sentiment label
# #         st.write("Sentiment:", sentiment_label)

# #     # st.title("Chatbot")
    
# # openai.api_key = st.secrets["api_secret"]

# # def generate_response(prompt):
# #     completions = openai.Completion.create(
# #         engine = "text-davinci-003",
# #         prompt = prompt,
# #         max_tokens = 1024,
# #         n =1,
# #         stop = None,
# #         temperature = 0.5,
# #     )
# #     message = completions.choices[0].text
# #     return message

# # st.title("ChatBot : Streamlit + openAI")

# # #storing the chat 

# # if 'past' not in st.session_state:
# #     st.session_state['past'] =[]
# # if 'generated' not in st.session_state:
# #     st.session_state['generated'] = []

# # def get_text():
# #     input_text = st.text_input("Enter your queries here", key="input")
# #     return input_text

# # user_input = get_text()

# # if user_input:
# #     output = generate_response(user_input)
# #     #store the output
# #     st.session_state.generated.append(output)
# #     st.session_state.past.append(user_input)

# # if st.session_state['generated']:
# #     for i in range(len(st.session_state['generated'])-1, -1 , -1):
        
# #         message(st.session_state['past'][i],is_user=True , key=str(i)+'_user')
# #         message(st.session_state["generated"][i] , key=str(i))
    

    
# # if __name__ == '__main__':
# #     main()
