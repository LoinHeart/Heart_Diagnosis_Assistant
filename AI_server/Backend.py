import pickle
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify,redirect
import joblib

app = Flask(__name__)

# Load the saved Keras model and Scaler
model = tf.keras.models.load_model('Test_Accuracy_84.91%.keras')

# Load the scaler (ensure it's in the same directory)
with open('scaler.pkl', 'rb') as f:
    scaler = joblib.load(f)

@app.route('/')
def home():
    return redirect("http://localhost:8501")


@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    data = request.json
    features = np.array([[
        data['age'], data['sex'], data['cp'], data['trestbps'], data['chol'], 
        data['fbs'], data['restecg'], data['thalach'], data['exang'], 
        data['oldpeak'], data['slope'], data['ca'], data['thal']
    ]])

    # Scale the input data
    scaled_features = scaler.transform(features)

    # Make a prediction
    prediction = model.predict(scaled_features)
    print("==",prediction,"\n")
    #Get the confidence level
    prediction_probs = model.predict(scaled_features)[0][0]
    
    predicted_class=float(prediction)
    print("==",prediction,"\n")
    # Return the result as JSON
    return jsonify({
        'predicted_class': 'No Heart disease.' if predicted_class<.5 else 'Heart disease.',  # Convert to float for JSON serialization
        'confidence': float(prediction_probs),
        'message': 'You are unlikely to have heart disease.' if predicted_class <0.5 else 'You are likely to have heart disease.'
    })

if __name__ == '__main__':
    app.run(debug=True)
