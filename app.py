from flask import Flask, render_template
import pandas as pd
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

app = Flask(__name__)

# Read data from the provided CSV file
df = pd.read_csv('ielts_writing_dataset.csv')

# Identify the correct column name containing the essays
essay_column_name = 'Essay'

# Function to extract key phrases from an essay
def extract_key_phrases(essay):
    sentences = sent_tokenize(essay)
    words = [word_tokenize(sentence) for sentence in sentences]

    # Filter out stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [[word.lower() for word in sentence if word.isalnum() and word.lower() not in stop_words] for sentence in words]

    # Part-of-speech tagging
    tagged_words = [pos_tag(sentence) for sentence in filtered_words]

    # Extract noun phrases
    key_phrases = []
    for tagged_sentence in tagged_words:
        key_phrases.extend([word for word, tag in tagged_sentence if tag.startswith('NN')])

    return key_phrases

# Function for sentiment analysis using VADER
def analyze_sentiment(essay):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(essay)

    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# AI-Based Test Case Generation
def generate_test_case():
    # Randomly select an essay from the dataset
    essay_index = random.randint(0, len(df) - 1)
    essay = df.iloc[essay_index][essay_column_name]

    # Generate expected results
    expected_key_phrases = extract_key_phrases(essay)
    expected_sentiment = analyze_sentiment(essay)

    return {
        'essay_index': essay_index,
        'essay': essay,
        'expected_key_phrases': expected_key_phrases,
        'expected_sentiment': expected_sentiment
    }

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling essay analysis
@app.route('/analyze_essay/<int:essay_index>')
def analyze_essay(essay_index):
    essay = df.iloc[essay_index][essay_column_name]

    # Extract key phrases
    key_phrases = extract_key_phrases(essay)
    detokenized_phrases = TreebankWordDetokenizer().detokenize(key_phrases)

    # Perform sentiment analysis
    sentiment = analyze_sentiment(essay)

    return render_template('index.html', essay=essay, key_phrases=detokenized_phrases, sentiment=sentiment, essay_index=essay_index)

# Route for AI-based test case generation
@app.route('/generate_test_case')
def generate_test_case_route():
    test_case = generate_test_case()
    return render_template('test_case.html', test_case=test_case)

if __name__ == '__main__':
    app.run(debug=True)
