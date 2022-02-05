import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjhhMzYyYWNjOTkyMmFjZjZmMDQyMjg0MWY5MDQyZCIsInN1YiI6IjYxZjk2Yjk3Y2NiMTVmMDBmYWY3YjZjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TXxYbka8zfyBryDlpse5tbyTG1GETiOrFqXYNIJwGNc"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

    

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_backdrop_url(backdrop_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]
    

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()