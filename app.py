from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load ML model and data
try:
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    car_data = pd.read_csv('Cleaned_Car_data.csv')
except Exception as e:
    model = None
    car_data = None
    print(f"Error loading model or data: {e}")

@app.route("/", methods=['GET'])
def home():
    return "Hello from backend!!!"

@app.route("/check-api", methods=['GET'])
def check():
    return "The api is working for this endpoint"

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model is not loaded. Please check server setup.'}), 500

    try:
        data = request.json
        company = data.get('company')
        car_model = data.get('car_model')
        year = int(data.get('year'))
        fuel_type = data.get('fuel_type')
        driven = int(data.get('kms_driven'))

        if not all([company, car_model, year, fuel_type, driven]):
            return jsonify({'error': 'All fields are required.'}), 400

        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
        return jsonify({'predicted_price': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': f'An error occurred during prediction: {str(e)}'}), 500
