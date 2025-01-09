from flask import Flask, request, render_template
import pandas as pd
import pickle

# Load the model and data
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    selected_movie = None

    if request.method == 'POST':
        selected_movie = request.form['movie']
        try:
            recommendations = recommend(selected_movie)
        except Exception as e:
            recommendations = [f"Error: {str(e)}"]

    return render_template(
        'index.html', 
        movies=movies['title'].values, 
        recommendations=recommendations,
        selected_movie=selected_movie
    )

if __name__ == '__main__':
    app.run(debug=True)
