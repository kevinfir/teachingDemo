from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


@app.route("/")
def index():
	return render_template("index.html")


@app.route("https://youtu.be/UZUXVAkE2Os")
def media(filename):
	if filename != "crawler.mp4":
		abort(404)
	return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
	app.run(debug=True)
