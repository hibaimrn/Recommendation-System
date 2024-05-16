from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Load the data
data = pd.read_csv('recommendation_data.csv')

# Create a TF-IDF vectorizer to convert text features into numerical vectors
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['reviewText'].values.astype('U'))

# Compute cosine similarities between all items using the TF-IDF vectors
item_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get top N similar items based on cosine similarity
def get_similar_items(item_id, top_n=5):
    item_index = data[data['asin'] == item_id].index[0]
    similar_indices = item_similarities[item_index].argsort()[::-1][1:top_n+1]
    similar_items = data.iloc[similar_indices]['asin'].values
    return similar_items.tolist()

@app.route('/', methods=['GET', 'POST'])
def recommend_items():
    if request.method == 'POST':
        item_id = request.form['asin']
        top_n = int(request.form['top_n'])
        similar_items = get_similar_items(item_id, top_n)
        return render_template('recommendation.html', items=similar_items)
    return render_template('recommendation.html', items=[])

if __name__ == '__main__':
    app.run(debug=True)
