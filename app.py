from flask import Flask, render_template, request
import joblib
from detector import check_url
from url_features import extract_features
import numpy as np
import datetime

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    rule_status = None
    risk_score = None
    reasons = None
    ml_label = None
    final_result = None
    confidence = None

    if request.method == "POST":
        url = request.form["url"]

        rule_status, risk_score, reasons = check_url(url)

        features = extract_features(url)
        features = np.array(features).reshape(1, -1)

        ml_prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        confidence = round(max(probabilities) * 100, 2)

        if ml_prediction == -1:
            ml_label = "PHISHING (ML Model)"
        else:
            ml_label = "LEGITIMATE (ML Model)"

        # Final Hybrid Decision
        if ml_prediction == -1 and risk_score >= 3:
            final_result = "HIGH RISK"
        elif ml_prediction == -1:
            final_result = "MEDIUM RISK"
        elif risk_score >= 3:
            final_result = "MEDIUM RISK"
        elif risk_score > 0:
            final_result = "LOW RISK"
        else:
            final_result = "SAFE"

        # Save scan history
        with open("scan_history.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | {url} | {final_result} | Confidence: {confidence}%\n")

    return render_template(
        "index.html",
        rule_status=rule_status,
        risk_score=risk_score,
        reasons=reasons,
        ml_result=ml_label,
        final_result=final_result,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)
