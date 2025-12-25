import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\singh\OneDrive\Desktop\movie_rec\tmdb_5000_credits.csv")

movies = load_data()

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
# Page background styling
page_bg_img = """
<style>
.stApp {
    background-image: url("https://img.freepik.com/free-photo/copy-space-clipboard-with-lighbox-beside_23-2148470136.jpg?semt=ais_hybrid&w=740&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
tfidf = TfidfVectorizer(stop_words='english')
text_column = None

for col in ['title', 'cast', 'crew']:
    if col in movies.columns:
        text_column = col
        break

if text_column is None:
    st.error("No text column found title or cast or crew")
    st.stop()

tfidf_matrix = tfidf.fit_transform(movies[text_column])


# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in movies['title'].values:
        return []

    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]

    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="🎬 Movie Recommendation System", layout="centered")

st.title("🎥 Movie Recommendation System")
st.write("Get movie recommendations based on content similarity.")

movie_list = movies['title'].tolist()
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommend_movies(selected_movie)

    if len(recommendations) > 0:
        st.subheader("🎯 Recommended Movies:")
        for movie in recommendations:
            st.write("✅", movie)
    else:
        st.warning("No recommendations found.")
