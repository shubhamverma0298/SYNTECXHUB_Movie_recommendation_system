from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load the data exported from the notebook
# Ensure these files are in your directory
movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    # You can get your own API key at https://www.themoviedb.org/settings/api
    api_key = "ea29c832998d132bfb8214127f361597" 
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        # Fallback image if API fails
        return "https://via.placeholder.com/500x750?text=No+Poster+Found"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        # Fetch movie_id to get the poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_list = movies['title'].tolist()
    recommendations = []
    selected_movie = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie_name')
        if selected_movie:
            names, posters = recommend(selected_movie)
            # Zip them together so we can iterate through both in the HTML template
            recommendations = zip(names, posters)

    return render_template('index.html', 
                           movie_list=movie_list, 
                           recommendations=recommendations,
                           selected_movie=selected_movie)

if __name__ == '__main__':
    app.run(debug=True)