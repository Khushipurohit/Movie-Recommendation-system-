import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_overview = []

    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_overview.append(movies.iloc[i[0]].overview)


    return recommended_movie_names,recommended_movie_posters,recommended_movie_overview

movie_list = pickle.load(open('movie_list.pkl', 'rb'))

movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

col1, mid, col2 = st.columns(3)

with mid:
       st.image('https://i.postimg.cc/tR12B5x9/big-open-clapper-board-movie-reel-cinema-icon-set-movie-film-elements-flat-design-cinema-movie-time.png', width = 300)
st.markdown("<h1 style='text-align: center; color: white; font: Serif'> MOVIE RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
'SELECT A MOVIE',
    movies['title'].values)

if st.button('Recommend'):

    recommended_movie_names,recommended_movie_posters,recommended_movie_overview = recommend(selected_movie_name)

    col1,col2, col3 = st.columns(3)
    with col2:
        st.write(recommended_movie_names[0])
    st.markdown(
        '<style>.ReactVirtualized_GridinnerScrollContainer div[class^="row"], .ReactVirtualizedGrid_innerScrollContainer div[class^="data row"]{ color:red; } </style>',
        unsafe_allow_html=True)
    cols1, col2,col3 = st.columns(3)
    with col2:
        st.image(recommended_movie_posters[0])


    cols1,col2= st.columns([10,1])
    with cols1:
        st.write(recommended_movie_overview[0])

    col1, col2, col3 = st.columns(3)
    with col2:
        st.write(recommended_movie_names[1])
        st.markdown(
            '<style>.ReactVirtualized_GridinnerScrollContainer div[class^="row"], .ReactVirtualizedGrid_innerScrollContainer div[class^="data row"]{ background:black; } </style>',
            unsafe_allow_html=True)

    cols1, col2, col3 = st.columns(3)
    with col2:
        st.image(recommended_movie_posters[1])

    cols1, col2 = st.columns([10, 1])
    with cols1:
        st.write(recommended_movie_overview[1])

    col1, col2,col3 = st.columns(3)
    with col2:
        st.write(recommended_movie_names[2])
        st.markdown(
            '<style>.ReactVirtualized_GridinnerScrollContainer div[class^="row"], .ReactVirtualizedGrid_innerScrollContainer div[class^="data row"]{ background:black; } </style>',
            unsafe_allow_html=True)

    cols1, col2, col3 = st.columns(3)
    with col2:
        st.image(recommended_movie_posters[2])

    cols1, col2 = st.columns([10, 1])
    with cols1:
        st.write(recommended_movie_overview[2])

    col1, col2, col3 = st.columns(3)
    with col2:
        st.write(recommended_movie_names[3])
        st.markdown(
            '<style>.ReactVirtualized_GridinnerScrollContainer div[class^="row"], .ReactVirtualizedGrid_innerScrollContainer div[class^="data row"]{ color: #FF4B4B ; font: Serif } </style>',
            unsafe_allow_html=True)

    cols1, col2, col3 = st.columns(3)
    with col2:
        st.image(recommended_movie_posters[3])

    cols1, col2 = st.columns([10, 1])
    with cols1:
        st.write(recommended_movie_overview[3])

    col1, col2, col3 = st.columns(3)
    with col2:
        st.write(recommended_movie_names[4])
        st.markdown(
            '<style>.ReactVirtualized_GridinnerScrollContainer div[class^="row"], .ReactVirtualizedGrid_innerScrollContainer div[class^="data row"]{ background:black; } </style>',
            unsafe_allow_html=True)

    cols1, col2, col3 = st.columns(3)
    with col2:
        st.image(recommended_movie_posters[4])

    cols1, col2 = st.columns([10, 1])
    with cols1:
        st.write(recommended_movie_overview[4])

activities = ["ABOUT PROJECT", "CONTACT ME", "ABOUT ME"]
choice  = st.sidebar.selectbox("Project Details Section", activities)

if choice == 'ABOUT PROJECT':
    st.sidebar.write("This is a movie Recommendation System when you select an movie then it will recommend 5 movies which are similar to the selected movie. I made this project by using of Python programming language and sstreamlit. ")


elif choice == 'CONTACT ME':
    st.sidebar.write("Get in touch with me!")

    col1,col2 = st.columns(2)
    with col1:
        st.sidebar.write("[LinkedIn Profile](https://www.linkedin.com/in/khushi-purohit-a3739a201/)")
        st.sidebar.write("[Github Profile](https://github.com/Khushipurohit)")
        st.sidebar.write("khushisvpurohit@gmail.com")

elif choice == 'ABOUT ME':
    col1, mid, col2 = st.columns([1, 1, 20])

    with col1:
        st.sidebar.image('https://i.postimg.cc/0ytSgTTF/IMG-20220529-092154.jpg',width= 200)
        st.sidebar.write("I am CSE sophomore at M.B.M Engineering University, Jodhpur. I am a Young Tech Enthusiast and a passionate learner. My vision in life is to bring significant changes across the globe through my tech creations. I have a knowledge of programming languages like C, C++, java. I have learnt front end web development. And currently learning Data Structure and algorithm. I have also keen intrest in Competitive programming and currently practicing it in codechef, codeforces and leetcode.")



