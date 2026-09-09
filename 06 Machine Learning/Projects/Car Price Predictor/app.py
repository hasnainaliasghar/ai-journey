import os
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
file_path = os.path.join(os.path.dirname(__file__), "CleanedCSV.csv")
model_path = os.path.join(os.path.dirname(__file__), "LinearRegressionModel.pkl")
car = pd.read_csv(file_path)

model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_model=car_model, years=year, fuel_types=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kms_driven'))

    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven,fuel_type]], columns=['name','company', 'year', 'kms_driven', 'fuel_type']))
    print(prediction)
    return "Rs." + str(prediction[0].round(2))

if __name__ == '__main__':
    app.run(debug=True, port=5500)