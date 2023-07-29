import streamlit as st
# import pickle

# # Load the sentiment analysis function from the pickle file
# with open('sentiment_analysis_model.pkl', 'rb') as file:
#     get_sentiment_label = pickle.load(file)
import dill

# Load the sentiment analysis function from the dill file
with open('sentiment_analysis_model.pkl', 'rb') as file:
    get_sentiment_label = dill.load(file)

def main():
    # Set a title for the app
    st.title("Sentiment Analysis Web App")

    # Get input text from the user
    user_input = st.text_area("Please enter your sentence:")

    # Check if the user has entered any text
    if user_input:
        # Call the sentiment analysis function to get the sentiment label
        sentiment_label = get_sentiment_label(user_input)

        # Display the sentiment label
        st.write("Sentiment:", sentiment_label)

if __name__ == '__main__':
    main()
