# **Movie Recommendation System 🎬**
This repository contains a **Movie Recommendation System** built with Python and **Streamlit**. The system uses a content-based filtering approach to recommend movies similar to the one selected by the user. The interactive web interface allows users to easily search for and explore movie recommendations.

## Features
  - **Content-Based Filtering:** Recommends movies based on their metadata (genres, cast, crew, keywords, and overview).
  - **Interactive UI:** Built using streamlit with a dark/light theme toggle.
  - **Efficient Search:** Uses a CountVectorizer and Cosine Similarity to find similar movies.

## How It Works
  1. **Data Processing:**
     - Merges movie metadata and credits datasets from TMDB.
     - Extracts relevant features (genres, keywords, cast, crew, and overview).
     - Preprocesses text data by tokenizing, stemming, and removing spaces.
     - Combines all processed features into a single "tag" for each movie.
  2. **Recommendation Engine:**
     - Vectorizes the "tags" using **CountVectorizer**.
     - Computes **cosine similarity** between movies based on their tags.
     - Recommends top 5 similar movies based on the similarity score.
  3. **Web Application:**
     - Users can search for a movie and get recommendations displayed interactively.
     - Includes a theme toggle for dark and light modes.

## Prerequisites
  - Python 3.x
  - strteamlit
  - Pandas, NumPy
  - Scikit-learn
  - NLTK
  - TMDB dataset [download here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Setup and Installation ⚙️
  1. **Clone the Repository:**
```
git clone https://github.com/Aashu-Raj/movie_recommendation_system.git
cd movie_recommendation_system
```

  2. Create and activate a virtual environment (Windows PowerShell):
```
python -m venv myenv
myvenv\Scripts\Activate
```

  3. Install dependencies:
```
pip install -r requirements.txt
```

  4. Dataset and model
- If `movies.pkl` and `similarity.pkl` exist in the repo root, the Streamlit app will use them directly.
- To regenerate these files, open and run `movie_recomendation_model.ipynb` which walks through downloading (Kaggle), preprocessing, and saving the processed data and similarity matrix.
- If you need to use Kaggle to download the dataset, place `kaggle.json` in `%USERPROFILE%/.kaggle/` on Windows.

  5. Run the Streamlit app
Start the app locally with:
```
streamlit run app_streamlit.py
```
Open the URL Streamlit prints (usually http://localhost:8501) and use the search box to get recommendations.

## Notebook
- `movie_recomendation_model.ipynb` contains the preprocessing steps, feature engineering, and model building. Run the notebook to reproduce `movies.pkl` and `similarity.pkl`.

## File Structure
```
movie_recommendation_system/
├── app_streamlit.py                    # Streamlit application code
├── movie_recomendation_model.ipynb     # Notebook for preprocessing & model building
├── requirements.txt                    # Python dependencies
├── kaggle.json                         # (Optional) Kaggle credentials for dataset download
├── movies.pkl                          # Serialized processed movie data
├── similarity.pkl                      # Serialized similarity matrix
└── README.md                           # This file
```

## Troubleshooting
- If Streamlit cannot find `movies.pkl` or `similarity.pkl`, run the notebook to create them.
- If you get missing package errors, ensure you installed `requirements.txt` inside the activated virtualenv.

````

