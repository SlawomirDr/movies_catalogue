from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

import tmdb_client

@app.route("/")
def homepage():
    movie_lists = ["now_playing", "popular", "top_rated", "upcoming"]
    selected_list = request.args.get('list_type')
    if selected_list not in movie_lists:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, movie_lists=movie_lists, selkected_list=selected_list)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def utility_processor():    
    def tmdb_post_url(path,size):
        return tmdb_client.get_backdrop_url(path, size)
    return {"tmdb_post_url": tmdb_post_url}
            


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)["cast"]
    movie_images = tmdb_client.get_movie_images(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=movie_images)

@app.context_processor
def utility_processor():
    def tmdb_backdrop_url(path, size):
        return tmdb_client.get_backdrop_url(path, size)  
    return {"tmdb_backdrop_url": tmdb_backdrop_url}  


if __name__ == '__main__':
    app.run(debug=True)