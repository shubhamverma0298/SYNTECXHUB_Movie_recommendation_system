# Movie Recommender System 🎬

A full-stack machine learning application that recommends movies based on content similarity. The system analyzes a dataset of 5,000 movies to find patterns in metadata and serves recommendations through a responsive web interface.


## 🚀 Features

* **Content-Based Filtering:** Uses Natural Language Processing (NLP) to recommend movies based on tags.
* **Dynamic Poster Fetching:** Integrates with **TMDB API** to display real-time movie posters.
* **Interactive Web UI:** A dark-themed, user-friendly interface built with Flask and Jinja2 templates.
* **Optimized Search:** Efficiently handles a large list of movie titles via a searchable dropdown.

## 🛠️ Tech Stack

* **Machine Learning:** Python, Pandas, Scikit-learn (CountVectorizer & Cosine Similarity), NLTK (PorterStemmer).
* **Backend:** Flask.
* **Frontend:** HTML5, CSS3 (Netflix Red theme).
* **Data Storage:** Pickle (for serialized model and dataframes).
* **API:** TMDB (The Movie Database).

## 📊 How It Works

1. **Data Preprocessing:** Metadata (genres, keywords, cast, crew) is cleaned and merged into a single "tags" column.
2. **Vectorization:** The text tags are converted into vectors using **Bag of Words** (`CountVectorizer`).
3. **Similarity Scoring:** **Cosine Similarity** is calculated between all movie vectors to determine how "close" movies are to each other in a 5,000-dimensional space.
4. **Recommendation:** When a movie is selected, the system finds the 5 movies with the highest similarity scores.

## 📋 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

```

### 2. Install Dependencies

Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt

```

### 3. Generate the Data Files

Run the Jupyter Notebook (`Task_1.ipynb`) to process the raw datasets and generate the required `.pkl` files:

* `movie_dict.pkl`
* `similarity.pkl`

### 4. Run the Application

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000`.

## 🔑 API Configuration

The app uses the TMDB API to fetch posters. A default key is provided in `app.py`, but for production or heavy use, please get your own:

1. Visit [The Movie Database API](https://www.themoviedb.org/settings/api).
2. Replace the `api_key` variable in `app.py` with your unique key.

## 📂 Project Structure

* `app.py`: Flask application logic and API integration.
* `Task_1.ipynb`: Data cleaning, EDA, and model building.
* `templates/index.html`: Web interface.
* `requirements.txt`: List of Python libraries needed.
* `movie_dict.pkl` & `similarity.pkl`: Pre-computed similarity matrices.

