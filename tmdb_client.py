from flask import request
import requests 
import random

import os
API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")


#def get_popular_movies():
 #   endpoint = "https://api.themoviedb.org/3/movie/popular"
  #  api_token = API_TOKEN
   # headers = {
    #    "Authorization": f"Bearer {api_token}"
   # }
   # response = requests.get(endpoint, headers=headers)
   # return response.json()

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_backdrop_url(backdrop_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_api_path}"


def get_movies(how_many, list_type):
   # selected_list = request.args.get('list_type', "popular")
   # movie_types = ['popular', 'top rated', 'upcoming', 'now playing']
   # if not list_type in movie_types:
   #     list_type = 'popular'
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")
    


def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits") #["cast"]
    

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")