# **Movie Recommendation System 🎬**
This repository contains a **Movie Recommendation System** built with Python and deployed using Flask. The system uses a content-based filtering approach to recommend movies similar to the one selected by the user. The application is deployed on **Render**, and the web interface allows users to interactively explore movie recommendations.

## Features
  - **Content-Based Filtering:** Recommends movies based on their metadata (genres, cast, crew, keywords, and overview).
  - **Interactive UI:** Built using streamlit with a dark/light theme toggle.
  - **Deployment:** Hosted on Render for easy accessibility.
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
     - Recommends top 5 similar movies.
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
  2. **Install dependencies:**
```
!pip install -r requirements.txt
```
  3. **Place the 'kaggle.json' file in the correct location and download the TMDB dataset:**
```
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d tmdb/tmdb-movie-metadata
```
  4. **Extract the dataset:**
```
````markdown
# Movie Recommendation System 🎬

This repository provides a content-based Movie Recommendation System implemented in Python. It includes a Streamlit demo (`app_streamlit.py`) for an interactive UI and a Jupyter notebook (`movie_recomendation_model.ipynb`) used to build and preprocess the recommendation model.

**Note:** The original README referenced a Flask app and a Render deployment. This repo contains a Streamlit app; instructions below reflect how to run the Streamlit interface locally.

## Features
- Content-based recommendations using movie metadata (genres, cast, crew, keywords, overview).
- Simple interactive UI using Streamlit for searching and showing similar movies.
- Model and preprocessing available in a Jupyter notebook for reproducibility.

## How It Works
1. Data preprocessing combines relevant text fields into a single "tag" per movie.
2. Tags are vectorized (e.g. CountVectorizer) and cosine similarity is computed between movies.
3. For a selected movie, the system returns the top-N most similar titles.

## Prerequisites
- Python 3.8+ (3.10 recommended)
- pip
- (Optional) Kaggle CLI if you want to re-download the TMDB dataset

## Setup — Windows (recommended)
1. Clone the repository:

```bash
git clone https://github.com/Aashu-Raj/movie_recommendation_system.git
cd movie_recommendation_system
```
2. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or use .venv\Scripts\activate for cmd.exe
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset and model
- If `movies.pkl` and `similarity.pkl` exist in the repo root, the Streamlit app will use them directly.
- To regenerate these files, open and run `movie_recomendation_model.ipynb` which walks through downloading (Kaggle), preprocessing, and saving the processed data and similarity matrix.
- If you need to use Kaggle to download the dataset, place `kaggle.json` in `%USERPROFILE%/.kaggle/` on Windows and use the Kaggle CLI as described in the notebook.

## Run the Streamlit app
Start the app locally with:

```bash
streamlit run app_streamlit.py
```

Open the URL Streamlit prints (usually http://localhost:8501) and use the search box to get recommendations.

## Notebook
- `movie_recomendation_model.ipynb` contains the preprocessing steps, feature engineering, and model building. Run the notebook to reproduce `movies.pkl` and `similarity.pkl`.

## File Structure
```
movie_recommendation_system/
├── app_streamlit.py                    # Streamlit demo app
├── movie_recomendation_model.ipynb     # Notebook for preprocessing & model
├── requirements.txt                    # Python dependencies
├── kaggle.json                         # (Optional) Kaggle credentials for dataset download
├── movies.pkl                          # (Optional) Serialized processed movie data
├── similarity.pkl                      # (Optional) Serialized similarity matrix
├── README.md                           # This file
└── myenv/                              # (Optional) local virtualenv (not committed normally)
```

## Troubleshooting
- If Streamlit cannot find `movies.pkl` or `similarity.pkl`, run the notebook to create them.
- If you get missing package errors, ensure you installed `requirements.txt` inside the activated virtualenv.

````

