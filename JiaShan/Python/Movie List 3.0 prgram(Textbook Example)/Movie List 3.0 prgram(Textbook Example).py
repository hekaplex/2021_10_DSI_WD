import pickle

FILENAME = "movies.bin"

def write_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)

def read_movies():
    movies = []
    with open(FILENAME, "rb") as file:
        movies = pickle.load(file)
    return movies

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")    
    print()
