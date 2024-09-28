import pickle
import streamlit as st
import requests
from fuzzywuzzy import fuzz, process
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

file_path = 'model/'

# Load training data
Train_Data = pd.read_pickle(r"model/TrainData.pkl")
similarity = pd.read_pickle(r"model/similarity.pkl")
movies = pd.read_csv(r"dataset/movies.csv")

def fetch_poster(movie_name):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={movie_name}&utf8=1"
    search_response = requests.get(search_url).json()
    
    try:
        page_title = search_response['query']['search'][0]['title']
        page_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
        
        page_content_url = f"https://en.wikipedia.org/w/api.php?action=parse&page={page_title}&prop=text&format=json"
        content_response = requests.get(page_content_url).json()
        html_content = content_response['parse']['text']['*']
        
        soup = BeautifulSoup(html_content, 'html.parser')
        infobox = soup.find('table', class_='infobox')
        
        if infobox:
            img = infobox.find('img')
            if img:
                poster_path = "https:" + img['src']
                return poster_path
            
    except (IndexError, KeyError):
        return None

    return None

def recommend(movie_name):
    recommended_movie_names = []
    recommended_movie_posters = []

    movie_list_in_training = Train_Data.drop_duplicates(subset=["title"], keep="first")[["movieId", "title"]].reset_index(drop=True)   
    matches = process.extract(movie_name, movie_list_in_training["title"], scorer=fuzz.partial_ratio)
    
    if len(matches) == 0:
        return ["No Match Found"], [None]

    movie_id = movie_list_in_training.iloc[matches[0][2]]["movieId"]  
    similarity_scores = similarity[movie_id].toarray().ravel()   
    similar_movie_id_list = np.argsort(-similarity_scores)[0:11]     
    sm_df = movie_list_in_training[movie_list_in_training["movieId"].isin(similar_movie_id_list)]   
    movie_similarity = {movie_id: similarity_scores[movie_id] for movie_id in similar_movie_id_list}
    sorted_movie_ids = sorted(movie_similarity.keys(), key=lambda x: movie_similarity[x], reverse=True)
    
    for movie_id in sorted_movie_ids[1:]:
        recommended_movie_names.append(sm_df[sm_df["movieId"] == movie_id]["title"].values[0])
        recommended_movie_posters.append(fetch_poster(recommended_movie_names[-1]))  
        if len(recommended_movie_names) >= 10:
            break
            
    return recommended_movie_names, recommended_movie_posters

# Initialize session state if it doesn't exist
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
    st.session_state.selected_movie = None

st.header('Movie Recommender System')
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    st.session_state.selected_movie = selected_movie
    st.session_state.recommendations = recommend(selected_movie)

# Display recommendations if they exist
if st.session_state.recommendations:
    recommended_movie_names, recommended_movie_posters = st.session_state.recommendations
    st.header("Recommendations:")
    cols = st.columns(5)  # Create 5 columns
    for i in range(len(recommended_movie_names)):
        with cols[i % 5]:
            if recommended_movie_posters[i]:
                st.image(recommended_movie_posters[i], use_column_width=True)
            else:
                st.image("static/notfound.jpg", use_column_width=True)
            st.text(recommended_movie_names[i])
