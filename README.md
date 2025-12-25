👨‍💻 Author

Badal Singh



Email_id--singh.badal3375@gmail.com


Data Science & Machine Learning Enthusiast


🎬 Movie Recommendation System (Streamlit App)

This project is a Movie Recommendation System built using Python, Streamlit, and Machine Learning.
It uses pre-trained similarity matrices (.pkl files) to recommend movies based on content similarity.

🚀 Features

🎥 Movie recommendations using cosine similarity

⚡ Fast performance using precomputed .pkl files

🧠 Content-based filtering

🖥️ Clean and interactive Streamlit UI

📦 Ready-to-use files (no training required)

📁 Project Structure
movie-recommender/
│
├── app.py                  # Main Streamlit application
├── movie_list.pkl          # Pickle file containing movie data
├── similarity.pkl          # Pickle file containing similarity matrix
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation

📦 Dataset Info

movie_list.pkl → Contains movie titles and metadata

similarity.pkl → Precomputed cosine similarity matrix

These files are already trained and ready to use.

🛠️ Installation & Setup
1️⃣ Clone or Download Project
git clone <your-repo-link>
cd movie-recommender


OR download ZIP and extract it.

2️⃣ Install Required Libraries
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

🎯 How It Works

User selects a movie from the dropdown.

The system finds similar movies using cosine similarity.

Top recommended movies are displayed instantly.

🧠 Technologies Used

Python

Streamlit

Pandas

NumPy

Scikit-learn

Pickle

📸 Sample Output
🎬 Recommended Movies:
- Interstellar
- The Dark Knight
- Inception
- Avatar

📌 Future Enhancements

Add movie posters using TMDB API

Improve recommendation accuracy

Add collaborative filtering

Deploy on Streamlit Cloud

 
