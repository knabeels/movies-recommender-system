import pickle
import streamlit as st
import pandas as pd
# load the pickle files for the similarity matrix and the movies dataframe
# The pickle files are created in the movie_recommender.py file
# The similarity matrix is a matrix of cosine similarities between all the movies
# The movies dataframe is a dataframe of all the movies in the dataset

# Here we define a function to recommend movies based on the selected movie name
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # index[0] gets first title that matches index 0
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Here we upload the pickle dump Similarity Model
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Here we upload the pickle dump DataFrame
movies_list = pickle.load(open('movies.pkl', 'rb'))
# Here we create a pandas dataframe from the movies list
movies = pd.DataFrame(movies_list)
# Here we create a title for the web app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('List of Movies', movies['title'])
# Here we created a button to recommend movies based on the selected movie name
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)