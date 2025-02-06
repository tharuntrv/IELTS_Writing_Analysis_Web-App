# IELTS Writing Analysis Web App

## Overview

This is a Flask-based web application that analyzes IELTS writing essays. It performs:

- **Key phrase extraction** using NLTK's natural language processing capabilities.
- **Sentiment analysis** using the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool.
- **AI-based test case generation** to randomly select an essay and generate expected results.

## Features

- **Analyze Essays**: Extracts key phrases and determines sentiment.
- **Generate Test Cases**: Randomly selects an essay and generates expected key phrases and sentiment.
- **Interactive Web Interface**: Displays analysis results in a user-friendly format.

## Installation & Setup

### Prerequisites

Ensure you have Python installed (version 3.x recommended). You also need to install dependencies.

### Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/tharuntrv/IELTS_Writing_Analysis_Web-App.git
cd IELTS_Writing_Analysis_Web-App

```

2. Install dependencies:

```bash
pip install flask pandas nltk
```

3. Download required NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

```

4. Ensure you have the required dataset file __ielts_writing_dataset.csv__ in the project directory.

## Usage

1. Run the Flask application:

```bash
python app.py

```

2. Open your web browser and go to:

```ini
http://127.0.0.1:5000/

```

## API Routes

| Route | Method | Description |
|--------|--------|-------------|
| `/` | GET | Home page |
| `/analyze_essay/<int:essay_index>` | GET | Analyzes an essay by index |
| `/generate_test_case` | GET | Generates a test case with a random essay |

## File Structure

```ini
IELTS_Writing_Analysis_Web-App/
│-- app.py  # Main Flask application
│-- templates/
│   ├── index.html  # HTML template for the home page
│   ├── test_case.html  # HTML template for test case display
│-- ielts_writing_dataset.csv  # Dataset file containing IELTS essays

```

## Technologies Used

- **Flask**: Web framework for building the application.
- **NLTK**: Used for NLP tasks like tokenization, stopword removal, and sentiment analysis.
- **Pandas**: Handles CSV file reading and data manipulation.
- **HTML & Jinja2**: Used for rendering dynamic web pages.
