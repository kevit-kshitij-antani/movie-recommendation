import pickle


movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movie = input()
def recommend(movie):
    index = movies[movies['movie_id'] == movie].index[0]
    print(index)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(movies.loc[i[0]].movie_id)
        