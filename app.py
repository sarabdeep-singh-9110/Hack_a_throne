from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Dummy data for demonstration
data = pd.DataFrame({
    'age': [25, 45, 35, 50, 23, 34],
    'income': [50000, 100000, 75000, 120000, 48000, 80000],
    'investment_amount': [20000, 50000, 30000, 60000, 10000, 35000],
    'risk_tolerance': [1, 2, 1, 3, 1, 2],
    'portfolio_type': ['Conservative', 'Balanced', 'Balanced', 'Aggressive', 'Conservative', 'Balanced']
})

# Train a simple model for demonstration
X = data[['age', 'income', 'investment_amount', 'risk_tolerance']]
y = data['portfolio_type']
model = RandomForestClassifier()
model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    income = int(request.form['income'])
    investment_amount = int(request.form['investment_amount'])
    risk_tolerance = int(request.form['risk_tolerance'])

    features = [[age, income, investment_amount, risk_tolerance]]
    prediction = model.predict(features)[0]

    return jsonify({'portfolio_type': prediction})

if __name__ == '__main__':
    app.run(debug=True)