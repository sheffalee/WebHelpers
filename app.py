# Import the required libraries
import openai
import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
from scipy.special import softmax
import numpy as np

headers={
    "authorization":st.secrets["API_KEY"],
    "content-type":"application/json"
}

#Set the openai api key
openai.api_key = st.secrets["API_KEY"]


# Define a function to preprocess text
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# Define sentiment analysis model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Define a function to predict sentiment
def predict_sentiment(text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    highest_sentiment = config.id2label[ranking[-1]]
    return highest_sentiment

# Sentiment Analysis Section
st.title("Sentiment Analysis")
# User input for sentiment analysis
user_input_sentiment = st.text_input("Enter your reviews here")

if user_input_sentiment:
    # Perform sentiment analysis
    highest_sentiment = predict_sentiment(user_input_sentiment)

    # Apply styling based on sentiment
    sentiment_color_map = {
        "positive": "positive-sentiment",
        "negative": "negative-sentiment",
        "neutral": "neutral-sentiment"
    }
    sentiment_styling = sentiment_color_map.get(highest_sentiment, "neutral-sentiment")
    sentiment_text = f"{highest_sentiment.capitalize()} Sentiment"
    st.markdown(
        f'<div class="sentiment-result {sentiment_styling}">{sentiment_text}</div>',
        unsafe_allow_html=True
    )



# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Define a function to generate a response from OpenAI's GPT-3 model
def generate_response(prompt):
    # Create a completion using the GPT-3 engine
    completions = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT-3 engine
        prompt=prompt,              # The input prompt for the model
        max_tokens=1024,            # Maximum number of tokens in the response
        n=1,                        # Generate only one response
        stop=None,                  # No stopping criteria
        temperature=0.5,            # Control the randomness of the response
    )

    # Get the generated text from the response
    message = completions.choices[0].text
    return message

# Set up the Streamlit app title and styling
st.title("Welcome to Web Helpers App")
st.title("Chatbot")
st.markdown(
    """
    <style>
        /* Add custom CSS styling here */
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .chat-container {
            display: flex;
            flex-direction: column;  /* Display newer messages above */
            margin: 20px 0;
        }
        .user-message {
            align-self: flex-start;
            background-color: #008CBA;
            padding: 10px;
            border-radius: 10px;
            max-width: 60%;
            margin-top: 5px;
        }
        .chatbot-message {
            align-self: flex-end;
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 10px;
            max-width: 60%;
            margin-top: 5px;
        }
        .positive-sentiment {
            background-color: #4CAF50;
            color: #ffffff;
        }
        .negative-sentiment {
            background-color: #FF5733;
            color: #ffffff;
        }
        .neutral-sentiment {
            background-color: #008CBA;
            color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to get user input
def get_text():
    input_text = st.text_input("Let's chat here", key="input")
    return input_text

# Get user input
user_input = get_text()

# Generate and display responses
if user_input:
    chat_entry = {
        'user': user_input,
        'chatbot': generate_response(user_input)
    }
    st.session_state.chat_history.append(chat_entry)

# Display chat history
if st.session_state.chat_history:
    for entry in reversed(st.session_state.chat_history):
        st.markdown(
            f'<div class="chat-container">'
            f'<div class="user-message">{entry["user"]}</div>'
            f'<div class="chatbot-message">{entry["chatbot"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
