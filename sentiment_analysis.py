import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle

# Download VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

def get_sentiment_label(sentence):
    # Create a SentimentIntensityAnalyzer object
    sia = SentimentIntensityAnalyzer()

    # Get the sentiment polarity scores using SentimentIntensityAnalyzer
    scores = sia.polarity_scores(sentence)

    if scores['pos'] > scores['neg'] and scores['pos'] > scores['neu']:
        sentiment_label = 'positive'
    elif scores['neg'] > scores['pos'] and scores['neg'] > scores['neu']:
        sentiment_label = 'negative'
    else:
        sentiment_label = 'neutral'

    return sentiment_label

# Get input text from the user
user_input = input("Please enter your sentence: ")

# Print the user's input
print("Example: ", user_input)

# Get the sentiment label using the provided function
sentiment_label = get_sentiment_label(user_input)

# Print the sentiment label
print("Sentiment: ", sentiment_label)

# Serialize the function to create the pickle file
with open('sentiment_analysis_model.pkl', 'wb') as file:
    pickle.dump(get_sentiment_label, file)
