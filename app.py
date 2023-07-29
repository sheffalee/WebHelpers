import streamlit as st
import pickle
from sentiment_analysis import get_sentiment_label 

def main():
    # Set a title for the app
    st.title("Sentiment Analysis Web App")

    # Get input text from the user
    user_input = st.text_area("Enter your review here:")
    
    # Check if the user has entered any text
    if user_input:
        # Perform sentiment analysis and get the sentiment label
        sentiment_label = get_sentiment_label(user_input)

        # Display the sentiment label
        st.write("Sentiment:", sentiment_label)

if __name__ == '__main__':
    main()
