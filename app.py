from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

MODEL_PATH = "model/payments.pkl"
SCALER_PATH = "model/scaler.pkl"

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
else:
    model = None
    scaler = None


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None or scaler is None:
            raise Exception("Model or scaler not loaded")

        type_mapping = {
            "CASH_IN": 0,
            "CASH_OUT": 1,
            "DEBIT": 2,
            "PAYMENT": 3,
            "TRANSFER": 4
        }

        step = float(request.form["step"])
        type_val = type_mapping[request.form["type"]]
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])

        # 🔴 IMPORTANT: use ONLY 7 features first
        input_data = np.array([[
            step, type_val, amount,
            oldbalanceOrg, newbalanceOrig,
            oldbalanceDest, newbalanceDest
        ]], dtype=float)

        logging.debug(f"Input data shape: {input_data.shape}")

        input_data_scaled = scaler.transform(input_data)

        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(input_data_scaled)[0][1]
        else:
            prob = float(model.predict(input_data_scaled)[0])

        risk_reasons = []
        risk_boost = 0

        if amount > 200000:
            risk_boost += 0.10
            risk_reasons.append("Large transaction amount")

        if request.form["type"] in ["TRANSFER", "CASH_OUT"]:
            risk_boost += 0.10
            risk_reasons.append("High-risk transaction type")

        if oldbalanceOrg > 0 and (newbalanceOrig / oldbalanceOrg) < 0.2:
            risk_boost += 0.15
            risk_reasons.append("Sender balance drastically reduced")

        if oldbalanceDest == newbalanceDest:
            risk_boost += 0.25
            risk_reasons.append("Receiver balance unchanged after transfer")

        final_risk = min(prob + risk_boost, 1.0)

        if final_risk > 0.6:
            risk_level = "HIGH"
            color = "danger"
        elif final_risk > 0.3:
            risk_level = "MEDIUM"
            color = "warning"
        else:
            risk_level = "LOW"
            color = "success"

        return render_template(
            "predict.html",
            risk_level=risk_level,
            risk_score=round(final_risk * 100, 2),
            color=color,
            reasons=risk_reasons
        )

    except Exception as e:
        logging.exception("Prediction failed")
        return f"<h3>Prediction Error</h3><pre>{str(e)}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
