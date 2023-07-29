import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

