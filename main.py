from flask import Flask, render_template
from app.wordbank import FRUITS, ANIMALS, COUNTRIES, WordBank, choose_random
from app.story import STORY

PORT: int = 8000
WORDBANKS: dict[str, WordBank] = {"fruits": FRUITS, "animals": ANIMALS, "countries": COUNTRIES}

app = Flask(__name__)


# HTML pages
@app.route("/", methods=["GET"])
def home():
    """Renders the home page of the website."""
    return render_template("index.html")


@app.route("/reading", methods=["GET"])
def reading():
    """Renders the reading activity page of the website."""
    return render_template("reading.html")


@app.route("/spelling", methods=["GET"])
def spelling():
    """Renders the spelling activity page of the website."""
    return render_template("spelling.html")


@app.route("/customize", methods=["GET"])
def customize():
    """Renders the font customization page of the website."""
    return render_template("customize.html")


@app.route("/reading/<story>", methods=["GET"])
def storybank_api(story: str):
    """Renders a specific story selected from the reading page."""
    data = STORY.get(story)
    if data is None:
        return {"message": f"Story {story} does not exist."}, 400

    title, path = data
    story_contents = ""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            story_contents += f"<p>{line}</p>"

    return render_template("book.html", story=title, story_contents=story_contents)


# API
@app.route("/api/words/<wordbank>", methods=["GET"])
def wordbank_api(wordbank: str):
    """Returns a random word from the word bank category selected along with the path to its illustration."""
    chosen_bank = WORDBANKS.get(wordbank)
    if chosen_bank is None:
        return {"message": f"Word bank '{wordbank}' does not exist."}, 400

    word, path = choose_random(chosen_bank)
    return {"word": word, "path": path}, 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=PORT)
