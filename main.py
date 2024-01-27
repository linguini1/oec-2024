from flask import Flask, render_template

PORT: int = 8000

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/reading")
def reading():
    return render_template("reading.html")


@app.route("/spelling")
def spelling():
    return render_template("spelling.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=PORT, debug=True)
