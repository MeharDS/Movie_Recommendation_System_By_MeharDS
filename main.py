import streamlit as st
import pickle
import requests

movies=pickle.load(open('movie_list.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommand_poster(movie_id):
    url=  url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data= requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    complete_poster_path= "https://image.tmdb.org/t/p/w500/" + poster_path
    return  complete_poster_path
def recommandation(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1]) #enumerate() function adds a counter as the key of the enumerate object.
    recommanded_movies = []
    recommanded_poster = []

    for i in distances[1:6]:
        #fatch movie poster
        movie_id = movies.iloc[i[0]].id
        recommanded_poster.append(recommand_poster(movie_id))
        recommanded_movies.append(movies.iloc[i[0]].title)


    return recommanded_movies, recommanded_poster

movies_list = movies['title']
st.header('Movie Recomandation System')
selected_movie = st.selectbox(
    'Select or Type Movie Name',
    (movies_list))

if st.button('Show Recommendation'):
    recommanded_movies_name, recommanded_movies_poster =recommandation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommanded_movies_name[0])
        st.image(recommanded_movies_poster[0])
    with col2:
        st.text(recommanded_movies_name[1])
        st.image(recommanded_movies_poster[1])

    with col3:
        st.text(recommanded_movies_name[2])
        st.image(recommanded_movies_poster[2])
    with col4:
        st.text(recommanded_movies_name[3])
        st.image(recommanded_movies_poster[3])
    with col5:
        st.text(recommanded_movies_name[4])
        st.image(recommanded_movies_poster[4])
