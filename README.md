# **Movie Recommendation System 🎬**
This repository contains a **Movie Recommendation System** built with Python and deployed using Flask. The system uses a content-based filtering approach to recommend movies similar to the one selected by the user. The application is deployed on **Render**, and the web interface allows users to interactively explore movie recommendations.

# Features
  - **Content-Based Filtering:** Recommends movies based on their metadata (genres, cast, crew, keywords, and overview).
  - **Interactive UI:** Built using Flask and HTML/CSS with a dark/light theme toggle.
  - **Deployment:** Hosted on Render for easy accessibility.
  - **Efficient Search:** Uses a CountVectorizer and Cosine Similarity to find similar movies.

# How It Works
  1. **Data Processing:**
     - Merges movie metadata and credits datasets from TMDB.
     - Extracts relevant features (genres, keywords, cast, crew, and overview).
     - Preprocesses text data by tokenizing, stemming, and removing spaces.
     - Combines all processed features into a single "tag" for each movie.
  2. **Recommendation Engine:**
     - Vectorizes the "tags" using **CountVectorizer**.
     - Computes **cosine similarity** between movies based on their tags.
     - Recommends top 5 similar movies.
  3. **Web Application:**
     - Users can search for a movie and get recommendations displayed interactively.
     - Includes a theme toggle for dark and light modes.

# Prerequisites
  - Python 3.x
  - Flask
  - Pandas, NumPy
  - Scikit-learn
  - NLTK
  - TMDB dataset [download here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

# Setup and Installation ⚙️
  1. **Clone the Repository:**

```
git clone https://github.com/Aashu-Raj/movie_recommendation_system.git
cd movie_recommendation_system
```
  2. **Install dependencies:**
```
!pip install -r requirements.txt
```
  4. **Place the 'kaggle.json' file in the correct location and download the TMDB dataset:**
```
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d tmdb/tmdb-movie-metadata
```
  6. **Extract the dataset:**
```
!unzip tmdb-movie-metadata.zip
```
  8. **Run the preprocessing script:**
     Preprocess the data using the Python script in the model(movie_recommendation_model.ipynb)
  9. **Start the Flask server:**
     python app.py

# Deployment 🌐
The application is deployed on [Render](https://movie-recommendation-nq56.onrender.com).

# Usage
  1. Open the application in your browser(https://movie-recommendation-nq56.onrender.com).
  2. Enter a movie name in the search bar.
  3. Get a list of recommended movies.
  4. Toggle between light and dark themes for a better user experience.

# File Structure
```
movie-recommendation-system/
│
├── app.py                                   # Flask application
├── movie_recommendation_model.ipynb         # Preprocessing and recommendation model script
├── templates/
│   └── index.html                           # HTML and CSS for the web interface
├── movies.pkl                               # Serialized movie data
├── similarity.pkl                           # Serialized similarity matrix
├── requirements.txt                         # Dependencies
├── README.md                                # Project documentation
```

