from flask import Flask, render_template, request
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model and car data
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('cleaned car.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get unique companies, car models, years, and fuel types
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].unique())

    # Insert a placeholder option
    companies.insert(0, 'Select Company')
    
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))  # Ensure year is an integer
    fuel_type = request.form.get('fuel_type')
    driven = float(request.form.get('kilo_driven'))  # Ensure driven is a float

    # Create a DataFrame for prediction
    input_data = pd.DataFrame({
        'name': [car_model],
        'company': [company],
        'year': [year],
        'kms_driven': [driven],
        'fuel_type': [fuel_type]
    })

    # Make prediction
    prediction = model.predict(input_data)
    print(prediction)  # Print prediction for debugging

    return str(np.round(prediction[0], 2))

if __name__ == '__main__':
    app.run(debug=True)
