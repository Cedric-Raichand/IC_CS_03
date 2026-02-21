from flask import Flask, render_template, request
import joblib
from detector import rule_based_check
from url_features import extract_features

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    risk_score = None
    reasons = None
    ml_result = None

    if request.method == "POST":
        url = request.form["url"]

        # Rule-based
        result, risk_score, reasons = rule_based_check(url)

        # ML
        features = extract_features(url)
        prediction = model.predict(features)[0]

        if prediction == -1:
            ml_result = "PHISHING (ML Model)"
        else:
            ml_result = "LEGITIMATE (ML Model)"

    return render_template(
        "index.html",
        result=result,
        risk_score=risk_score,
        reasons=reasons,
        ml_result=ml_result
    )


if __name__ == "__main__":
    app.run(debug=True)