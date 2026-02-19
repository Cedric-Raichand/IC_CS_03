from flask import Flask, render_template, request
from detector import rule_based_detection

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        url = request.form.get("url")
        if not url.startswith("http"):
            url = "http://" + url

        verdict, score, reasons = rule_based_detection(url)

        result = {
            "url": url,
            "verdict": verdict,
            "score": score,
            "reasons": reasons
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

