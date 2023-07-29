import streamlit as st
import pickle
from sentiment_analysis import get_sentiment_label  # Import the function from sentiment_analysis.py
from chatbot import chatbot_response  # Import the chatbot_response function from chatbot.py

# openai.api_key = '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'

def main():
    # Set a title for the app
    st.title("Sentiment Analysis and Chatbot Web App")

    # Get input text from the user
    user_input = st.text_area("Enter your review here:")

    chat_input = st.text_area("Chat with the bot here:")
    
    # Check if the user has entered any text
    if user_input:
        # Perform sentiment analysis and get the sentiment label
        sentiment_label = get_sentiment_label(user_input)

        # Display the sentiment label
        st.write("Sentiment:", sentiment_label)

        # Prepare messages for chatbot
        messages = [{"role": "user", "content": user_input}]
        chatbot_reply = chatbot_response(messages)

        # Display the chatbot response in a separate input field
        st.text_input("Chatbot:", value=chatbot_reply, key="chatbot_input", disabled=True)

if __name__ == '__main__':
    main()

# import streamlit as st
# import pickle
# from sentiment_analysis import get_sentiment_label  # Import the function from sentiment_analysis.py
# from chatbot import chatbot_response  # Import the chatbot_response function from chatbot.py

# def main():
#     # Set a title for the app
#     st.title("Sentiment Analysis and Chatbot Web App")

#     # Get input text from the user
#     user_input = st.text_area("Please enter your sentence:")

#     # Check if the user has entered any text
#     if user_input:
#         # Perform sentiment analysis and get the sentiment label
#         sentiment_label = get_sentiment_label(user_input)

#         # Display the sentiment label
#         st.write("Sentiment:", sentiment_label)

#         # Prepare messages for chatbot
#         messages = [{"role": "user", "content": user_input}]
#         chatbot_reply = chatbot_response(messages)

#         # Display the chatbot response
#         st.markdown("Chatbot: " + chatbot_reply)

# if __name__ == '__main__':
#     main()

# # import streamlit as st
# # import pickle
# # from sentiment_analysis import get_sentiment_label  # Import the function from sentiment_analysis.py

# # def main():
# #     # Set a title for the app
# #     st.title("Sentiment Analysis Web App")

# #     # Get input text from the user
# #     user_input = st.text_area("Please enter your sentence:")

# #     # Check if the user has entered any text
# #     if user_input:
# #         # Call the sentiment analysis function to get the sentiment label
# #         sentiment_label = get_sentiment_label(user_input)

# #         # Display the sentiment label
# #         st.write("Sentiment:", sentiment_label)

# # if __name__ == '__main__':
# #     main()

# # import streamlit as st
# # import cloudpickle as cp

# # # Load the sentiment analysis function from the cloudpickle file
# # with open('sentiment_analysis_model.pkl', 'rb') as file:
# #     get_sentiment_label = cp.load(file)

# # def main():
# #     # Set a title for the app
# #     st.title("Sentiment Analysis Web App")

# #     # Get input text from the user
# #     user_input = st.text_area("Please enter your sentence:")

# #     # Check if the user has entered any text
# #     if user_input:
# #         # Call the sentiment analysis function to get the sentiment label
# #         sentiment_label = get_sentiment_label(user_input)

# #         # Display the sentiment label
# #         st.write("Sentiment:", sentiment_label)

# # if __name__ == '__main__':
# #     main()

# # # import streamlit as st
# # # # import pickle

# # # # # Load the sentiment analysis function from the pickle file
# # # # with open('sentiment_analysis_model.pkl', 'rb') as file:
# # # #     get_sentiment_label = pickle.load(file)
# # # import dill

# # # # Load the sentiment analysis function from the dill file
# # # with open('sentiment_analysis_model.pkl', 'rb') as file:
# # #     get_sentiment_label = dill.load(file)

# # # def main():
# # #     # Set a title for the app
# # #     st.title("Sentiment Analysis Web App")

# # #     # Get input text from the user
# # #     user_input = st.text_area("Please enter your sentence:")

# # #     # Check if the user has entered any text
# # #     if user_input:
# # #         # Call the sentiment analysis function to get the sentiment label
# # #         sentiment_label = get_sentiment_label(user_input)

# # #         # Display the sentiment label
# # #         st.write("Sentiment:", sentiment_label)

# # # if __name__ == '__main__':
# # #     main()
