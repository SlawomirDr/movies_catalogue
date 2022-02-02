from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ["Film", "Film2", "Film3", "Film4","Film5", "Film6", "Film7", "Film8"]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)