# Customer Churn Prediction - Flask App

This project is a **Customer Churn Prediction** web application built with **Flask**.  
It uses a machine learning model trained on the Telco Customer Churn dataset to predict whether a customer will churn based on their details.



## 📂 Project Structure
customer-churn-flask/
│
├── app.py # Flask application
├── model.pkl # Trained ML model
├── encoder.pkl # Label encoder for categorical features
├── expected_columns.pkl # Expected input columns for the model
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset
├── requirements.txt # Required dependencies
├── README.md # Project documentation
├── Capstone_Project_Presentation.pptx
├── templates/
  └── index.html # HTML form for user input

## How to Run Locally

### 1 Clone the repository
```
git clone https://github.com/YOUR_USERNAME/customer-churn-flask.git
cd customer-churn-flask
### 2 Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Mac/Linux
.venv\Scripts\activate     # On Windows
### 3 Install dependencies
pip install -r requirements.txt
### 4 Run the Flask app
python app.py
The app will be available at http://127.0.0.1:5000/
📊 Dataset
The dataset used is Telco Customer Churn from IBM Sample Data Sets.
It contains customer demographic, account, and service information.

🛠 Built With
Python
Flask
Pandas, NumPy
Scikit-learn
HTML/CSS (for the front-end)


Author
Sonu Tamang
📧 Email: your.email@example.com
🔗 LinkedIn: Your LinkedIn
💻 GitHub: Your GitHub

⚠ Limitations
Model trained on historical data; may not generalize perfectly.

Limited feature set (only certain customer attributes used).

Currently runs locally; not deployed online.

📌 License
This project is open-source under the MIT License.
