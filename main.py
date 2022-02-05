from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

import tmdb_client

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=8)
    return render_template("homepage.html", movies=movies)



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


#@app.movie_details
  #  def movie_id():




@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)




if __name__ == '__main__':
    app.run(debug=True)