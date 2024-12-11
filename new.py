import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Prompt user for domain
print("Enter the domain (e.g., garments, electronics, toys, shoes):")
domain = input().strip().lower()

domain_types = {
    "garments": ["summer clothing", "winter clothing", "all-season clothing"],
    "shoes": ["formal", "sports", "casual", "all-season"],
    "electronic devices": ["smartphones", "laptops", "home appliances", "gaming devices"],
    "toys": ["educational", "action figures", "puzzles", "outdoor games"],
    "furniture": ["living room", "bedroom", "outdoor", "office"],
}
for domain_category in domain_types.values() :
    print (domain_category)
print("Choose one type")
domain_category_lexicon=input()
# Garments types and associated keywords
garments = {
    "summer": {"lightweight": 3.0, "breathable": 2.5, "cool": 1.2},
    "winter": {"warm": 3.0, "thick": 2.5, "insulated": 2.8, "cozy": 2.5},
    "all-season": {"versatile": 2.5, "durable": 3.0, "all-season": 2.8},
}

# Shoes types and associated keywords
shoes = {
    "formal": {"elegant": 3.0, "professional": 2.8, "stylish": 2.5},
    "sports": {"lightweight": 3.0, "grip": 2.8, "flexible": 2.5},
    "casual": {"comfortable": 3.0, "relaxed": 2.8, "trendy": 2.5},
    "all-season": {"durable": 3.0, "versatile": 2.5, "weatherproof": 2.8},
}

# Electronic devices types and associated keywords
electronic_device = {
    "smartphones": {"innovative": 3.0, "user-friendly": 2.8, "fast": 2.5},
    "laptops": {"portable": 3.0, "powerful": 2.8, "efficient": 2.5},
    "home appliances": {"durable": 3.0, "energy-saving": 2.8, "modern": 2.5},
    "gaming devices": {"immersive": 3.0, "responsive": 2.8, "advanced": 2.5},
}

# Toys types and associated keywords
toys = {
    "educational": {"interactive": 3.0, "informative": 2.8, "engaging": 2.5},
    "action figures": {"detailed": 3.0, "heroic": 2.8, "fun": 2.5},
    "puzzles": {"challenging": 3.0, "creative": 2.8, "rewarding": 2.5},
    "outdoor games": {"active": 3.0, "fun": 2.8, "exciting": 2.5},
}

# Furniture types and associated keywords
furniture = {
    "living room": {"stylish": 3.0, "comfortable": 2.8, "modern": 2.5},
    "bedroom": {"cozy": 3.0, "relaxing": 2.8, "durable": 2.5},
    "outdoor": {"weatherproof": 3.0, "sturdy": 2.8, "versatile": 2.5},
    "office": {"ergonomic": 3.0, "professional": 2.8, "spacious": 2.5},
}


# Update lexicon based on domain
if domain in domain_types:
    if garments in  :
        custom_words = domaintype_lexicons[domain]
    analyzer.lexicon.update(custom_words)
    print(f"Custom lexicon updated for {domain}: {custom_words}")
else:
    print("Domain not recognized. Using default lexicon.")

# Test with a sentence
print("Enter a sentence to analyze:")
sentence = input()

# Perform sentiment analysis
scores = analyzer.polarity_scores(sentence)

compound_score=scores['compound']

print("Sentiment Scores:", scores)
if(compound_score >0.5) :
    print("Product is good")
elif(compound_score <=-0.5) :
    print("Product is average")
else :
    print("Product is bad")
