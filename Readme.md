
# 🛡️ Online Payments Fraud Detection using Machine Learning

A machine learning–based web application that detects **fraudulent online payment transactions** in real time using transaction data and behavioral patterns. Built with **Python, Scikit-learn, and Flask**, and deployed on **localhost**.


## 🚀 Features

* Real-time fraud prediction
* ML probability + rule-based risk scoring
* Explainable risk reasons
* Clean Flask web interface
* Modular and scalable project structure
* Localhost deployment (secure & offline)


## 🧠 Tech Stack

* **Python**
* **Flask**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **HTML, CSS (Bootstrap)**


## 📂 Project Structure

```
online_payments_fraud_detection/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── PS_20174392719_1491204439457_log.csv
│
├── model/
│   ├── payments.pkl
│   └── scaler.pkl
│
├── static/
│   ├── css/style.css
│   └── images/
│
├── templates/
│   ├── home.html
│   ├── submit.html
│   └── predict.html
│
├── training/
│   └── ONLINE_PAYMENTS_FRAUD_DETECTION.ipynb
│
└── training_ibm/
    └── online_payments_fraud_prediction_ibm.ipynb
```


## ⚙️ How It Works

1. User enters transaction details via the web UI
2. Input is preprocessed and scaled
3. ML model predicts fraud probability
4. Risk rules enhance prediction score
5. Final risk level is displayed:

   * **LOW**
   * **MEDIUM**
   * **HIGH**


## 🧪 Machine Learning Pipeline

* Data Collection
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Model Training & Evaluation
* Hyperparameter Tuning
* Model & Scaler Saving
* Flask Integration


## ▶️ Run Locally

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd online_payments_fraud_detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```


## 📊 Output

* Fraud risk percentage
* Risk level (LOW / MEDIUM / HIGH)
* Risk explanation reasons


## 🔐 Why This Project?

* Combines **ML + rule-based logic** for better accuracy
* Provides **explainable AI outputs**
* Demonstrates **end-to-end ML deployment**
* Ideal for **AI / ML / Full-Stack portfolios**


## 🛠️ Future Enhancements

* Database integration
* User authentication
* Real-time transaction streaming
* Cloud deployment
* Advanced anomaly detection models


## 👨‍💻 Author

**Online Payments Fraud Detection using Machine Learning**

Category: **Artificial Intelligence**

Deployment: **Localhost (Flask)**


## ⭐ Conclusion

This project showcases a practical application of machine learning in securing online payment systems by detecting fraudulent activities efficiently and transparently.


