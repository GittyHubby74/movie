from flask import Flask, render_template, request, jsonify
from recommender import recommend

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    movie = data.get("movie", "")

    results = recommend(movie)

    return jsonify({"recommendations": results})


if __name__ == "__main__":
    app.run(debug=True)