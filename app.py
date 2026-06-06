from flask import Flask, render_template, request, jsonify
from movies import GENRES, MOODS
from recommender import recommend

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", genres=GENRES, moods=MOODS)

@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.json
    genre = data.get("genre")
    mood = data.get("mood")
    industry = data.get("industry", "Both")

    movies = recommend(genre=genre, mood=mood, industry=industry)
    return jsonify(movies)

if __name__ == "__main__":
    app.run(debug=True)
