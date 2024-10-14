from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    items = [
        "Kopf",
        "Hals",
        "Schulter",
        "Rücken",
        "Brust",
        "Handgelenk",
        "Haende",
        "Gurt",
        "Hose",
        "Schuhe",
        "Fingereins",
        "Fingerzwei",
        "Schmuckeins",
        "Schmuckzwei",
    ]
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
