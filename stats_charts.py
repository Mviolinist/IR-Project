import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the preprocessed articles data
df = pd.read_csv("csv/preprocessed_articles.csv")

#df = df.head(100)

# Most frequent words
words = ' '.join(df['content']).split()
word_counts = pd.Series(words).value_counts()
most_frequent_words = word_counts.head(10)

# Histogram of word frequencies
plt.figure(figsize=(10, 6))
most_frequent_words.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Frequent Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Calculate cosine similarities between documents
contents = df['content']
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(contents)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create a heatmap for document similarities
plt.figure(figsize=(10, 6))
plt.imshow(cosine_sim, cmap='coolwarm', interpolation='nearest')
plt.title('Cosine Similarity Heatmap')
plt.colorbar()
plt.show()