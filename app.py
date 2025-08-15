#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pipeline
model = joblib.load('model.pkl')

# Load the expected columns from training
expected_columns = joblib.load('expected_columns.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    input_data = {
        'gender': request.form.get('gender'),
        'SeniorCitizen': int(request.form.get('SeniorCitizen')),
        'Partner': request.form.get('Partner'),
        'tenure': float(request.form.get('tenure')),
        'MonthlyCharges': float(request.form.get('MonthlyCharges')),
        'TotalCharges': float(request.form.get('TotalCharges'))
    }
    
    # Create DataFrame with expected columns
    df = pd.DataFrame([input_data])

    # Ensure all expected columns are present
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0  # or any default value used during training

    # Reorder columns to match training
    df = df[expected_columns]

    # Make prediction
    prediction = model.predict(df)[0]

    output = "Customer will Churn" if prediction == 1 else "Customer will Stay"

    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




