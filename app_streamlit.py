import streamlit as st
import pandas as pd
import pickle
import os

# --- Configuration ---
# Set the title and icon for the Streamlit app
st.set_page_config(page_title="Movie Recommender", layout="centered")

# --- Function Definitions (from original app.py) ---

@st.cache_resource
def load_data():
    """Loads the pickled model data and similarity matrix."""
    try:
        # Check if files exist
        if not os.path.exists('movies.pkl'):
            st.error("Error: 'movies.pkl' not found. Please ensure all model files are present.")
            return None, None
        if not os.path.exists('similarity.pkl'):
            st.error("Error: 'similarity.pkl' not found. Please ensure all model files are present.")
            return None, None
        
        # Load the dictionary of movies
        movies_dict = pickle.load(open('movies.pkl', 'rb'))
        movies_df = pd.DataFrame(movies_dict)
        
        # Load the similarity matrix
        similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
        
        return movies_df, similarity_matrix
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None

def recommend(movie, movies_df, similarity_matrix):
    """Generates movie recommendations based on cosine similarity."""
    try:
        # Get the index of the movie
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        
        # Get the similarity distances for the movie
        distance = similarity_matrix[movie_index]
        
        # Sort and get the top 5 (excluding the movie itself)
        movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        for i in movies_list:
            # Append the title of the recommended movie
            recommended_movies.append(movies_df.iloc[i[0]]['title'])
        
        return recommended_movies
    except IndexError:
        return [f"Movie '{movie}' not found in the database. Please select from the list or check the spelling."]
    except Exception as e:
        return [f"An unexpected error occurred during recommendation: {str(e)}"]

# --- Load Data and Initialize App ---

movies_df, similarity_matrix = load_data()

if movies_df is None or similarity_matrix is None:
    st.stop() # Stop the application if data loading failed

# Extract movie titles for the dropdown/select box
movie_titles = movies_df['title'].values

# --- Streamlit UI Design ---

st.title("Movie Recommendation System")

# Movie Selection Input
selected_movie_name = st.selectbox(
    "Search for a Movie:",
    movie_titles,
    index=None, # Start with no selection
    placeholder="Choose a movie...",
)

# Recommendation Button
if st.button("Get Recommendations"):
    if selected_movie_name:
        with st.spinner(f'Finding recommendations for **{selected_movie_name}**...'):
            # Call the recommendation function
            recommendations = recommend(selected_movie_name, movies_df, similarity_matrix)
        
        # Display Results
        st.subheader(f"If you liked **{selected_movie_name}**, you might also enjoy:")
        
        # Check for errors returned as a list
        if recommendations and recommendations[0].startswith("Error:"):
            st.error(recommendations[0])
        elif recommendations:
            # Display recommendations in a formatted box
            st.markdown('<div class="recommendations-box">', unsafe_allow_html=True)
            st.markdown("### Recommended Movies:")
            for i, movie in enumerate(recommendations, 1):
                st.markdown(f"**{i}.** {movie}")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("No recommendations found or an error occurred.")
    else:
        st.warning("Please select a movie to get recommendations.")
        
# Theme Toggle
st.markdown("---")
st.info("💡 Tip: Use the Settings menu (top right corner) to change the app's theme.")

if __name__ == '__main__':
    pass