from flask import Flask, render_template

PORT: int = 8000

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hi dyslexic person!!!1!</h1>"


if __name__ == "__main__":
    app.run("0.0.0.0", port=PORT, debug=True)
