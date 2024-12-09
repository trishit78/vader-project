import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Prompt user for domain
print("Enter the domain (e.g., garments, electronics, toys, shoes):")
domain = input().strip().lower()

# Define domain-specific lexicon adjustments
domain_lexicons = {
    "garments": {"stylish": 3.0, "uncomfortable": -2.5, "durable": 2.0},
    "electronics": {"innovative": 2.5, "outdated": -2.0, "efficient": 3.0},
    "toys": {"fun": 3.0, "educational": 2.5, "fragile": -2.0},
    "shoes": {"comfortable": 3.0, "stylish": 2.5, "tight": -1.5},
}

# Update lexicon based on domain
if domain in domain_lexicons:
    custom_words = domain_lexicons[domain]
    analyzer.lexicon.update(custom_words)
    print(f"Custom lexicon updated for {domain}: {custom_words}")
else:
    print("Domain not recognized. Using default lexicon.")

# Test with a sentence
print("Enter a sentence to analyze:")
sentence = input()

# Perform sentiment analysis
sentiment = analyzer.polarity_scores(sentence)
print("Sentiment Scores:", sentiment)
