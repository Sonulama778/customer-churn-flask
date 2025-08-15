# Customer Churn Prediction – Flask Web App
A Flask-based web application for predicting customer churn using a machine learning model.
This project is part of a capstone project that uses the Telco Customer Churn dataset to train and deploy a predictive model through a user-friendly interface.

## Features
Upload or enter customer details to get churn prediction.

Machine learning model trained on the Telco Customer Churn dataset.

Preprocessing pipeline including encoding, scaling, and feature alignment.

Flask backend serving predictions via a web interface.

Interactive Jupyter Notebook with exploratory data analysis (EDA) and model training steps.

## Project Structure
## 📂 Project Structure

```plaintext
customer-churn-flask/
│
├── templates/                     # HTML templates for the web app
│   └── index.html                  # Main UI page
│
├── app.py                          # Flask application script
├── Capstone_Project_Presentation.pdf # Project presentation slides
├── README.md                       # Project documentation
├── SonuTamang_CapstoneProject.ipynb # EDA and model training notebook
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
├── encoder.pkl                     # Encoded categorical features
├── scaler.pkl                      # Feature scaling object
├── expected_columns.pkl            # Expected feature columns for model input
├── model.pkl                       # Trained ML model
└── requirements.txt                # Python dependencies


# Installation & Setup
### Clone the repository

git clone https://github.com/Sonulama778/customer-churn-flask.git
cd customer-churn-flask

### Create a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### Install dependencies

pip install -r requirements.txt

### Running the Application

python app.py

The Flask app will start locally. Open your browser and go to:

http://127.0.0.1:5000/

## Model Information
### Algorithm: 

Machine Learning Classification (e.g., Logistic Regression / Random Forest – as implemented in the notebook)

### Dataset: 

Telco Customer Churn (features include demographics, account info, and services subscribed)

### Preprocessing:

Encoding categorical variables using encoder.pkl

Scaling numerical features using scaler.pkl

Aligning feature columns to match training data using expected_columns.pkl

## Workflow
Data Analysis & Model Training – Done in SonuTamang_CapstoneProject.ipynb

Model Export – Saved as model.pkl

Preprocessing Objects Exported – encoder.pkl, scaler.pkl, and expected_columns.pkl

Flask App Development – Implemented in app.py with HTML templates in /templates

Deployment – Can be hosted locally or deployed on platforms like Heroku, Render, or AWS.

## Prediction Flow
User inputs customer information via the web form.

Data is preprocessed using stored encoder, scaler, and expected column order.

Model predicts churn probability.

Result is displayed on the webpage.

## Requirements
The main dependencies include:

Flask==3.1.1

pandas==2.3.1

scikit-learn==1.7.1

numpy==2.2.6

matplotlib, seaborn (for analysis in notebook)

Full list available in requirements.txt.

## Future Improvements
Add user authentication for secure access.

Deploy to a cloud hosting service.

Enhance UI for better user experience.

Incorporate additional data sources for more accurate predictions.

## Author
Sonu Tamang
GitHub: Sonulama778
LinkedIn: [(https://www.linkedin.com/in/sonu-tamang/)]
