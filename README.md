# Heart_Diagnosis_Assistant
The Heart Diagnosis Assistant: is an AI-powered application designed to help you assess your heart health.

It analyzes your input data (such as age, cholesterol levels, and more) to provide a prediction on the likelihood of heart disease.

This tool is meant to offer insights into heart health, and to assist medical advice.

## Project Structure

- `Heart_Diagnosis_Assistant_FrontEnd/`
  - **`HDA.py`**: Streamlit script providing a user interface for interacting with the heart disease prediction result.

- `AI_server/`
  - **`Backend.py`**: Flask API server handling predictions. It processes data received from the Streamlit interface and returns prediction results.
  - **`Test_Accuracy_84.91%.keras`**: Trained Keras model file used for making predictions.
  - **`scaler.pkl`**: Scaler file for standardizing input features before making predictions.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/LoinHeart/Heart_Diagnosis_Assistant.git
   cd 'Heart_Diagnosis_Assistant'
2. **Set Up a Virtual Environment:**

It is recommended to use a virtual environment. You can create one using venv or conda, and then install the required packages.

**Create and activate the new virtual environment 'windows':**

         python -m venv HDA #create the virtual environment
         HDA\Scripts\activate  #Activate the virtual environment using cmd
        


          
  
3. **Install Dependencies:**


        pip install -r requirements.txt

4. **Run the AI Server:**

Navigate to the AI_server directory and start the server.


      cd AI_server
      python Backend.py
      The server will start and listen for requests on http://127.0.0.1:5000.

5. **Run the Heart_Diagnosis_Assistant:**

In a separate terminal, navigate to the Heart_Diagnosis_Assistant_FrontEnd directory and start the application.


        cd Heart_Diagnosis_Assistant_FrontEnd
        python -m streamlit run HDA.py
The Streamlit interface will be available at http://localhost:8501.

**Usage**

**Interacting with the Heart_Diagnosis_Assistant Interface:**

Open the app in your web browser.
Enter the required data (age, sex, chest pain type, etc.) into the provided fields.
Click the "Predict" button to obtain the heart disease prediction.

**Heart_Diagnosis_Assistant API Endpoint:**

Endpoint: /predict
Method: POST
Data: JSON object with the required features.
Response: JSON object containing the predicted class and a message indicating the likelihood of heart disease.

     
        {
          "age": 63,
          "sex": 1,
          "cp": 3,
          "trestbps": 145,
          "chol": 233,
          "fbs": 1,
          "restecg": 0,
          "thalach": 150,
          "exang": 0,
          "oldpeak": 2.3,
          "slope": 0,
          "ca": 0,
          "thal": 1
        }
 

**Example Response:**


      {
        "predicted_class": 1,
        "message": "You are likely to have heart disease."
      }

**`Notes`**

  -Ensure that Test_Accuracy_84.91%.keras and scaler.pkl are located in the AIserver directory before starting the Flask server.
  
  -Adjust paths and configurations as needed based on your environment.
  
**requirements.txt**

Here is the requirement.txt file listing all necessary packages:
   
      tensorflow==2.16.1
      scikit-learn==1.3.0
      flask==2.3.3
      joblib==1.3.2
      streamlit==1.22.0

**Instructions for Using requirements.txt**

Create a Virtual Environment (if not already created):

      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows, use `venv\Scripts\activate`'
      
**Install the Required Packages:**

        ```bash
        pip install -r requirement.txt'
This file ensures that all necessary dependencies for running the Heart Disease Diagnostic Chatbot are installed. Adjust package versions if needed based on your specific setup or compatibility requirements.



Dir Tree:

      Heart Disease Diagnostic Chatbot/
      │
      ├── AI_server/
      │   ├── __init__.py
      |   ├── Backend.py
      │   ├── Test_Accuracy_84.52%.keras
      │   └── scaler.pkl
      │
      ├── Chatbot/
      │   └── HDDC.py
      ├── final_project.ipynb  
      ├── __init__.py
      ├── heart_disease_uci.csv
      ├── requirement.txt
      └── README.md


**interact with AI_server backend without using Heart_Diagnosis_Assistant web interface**

you can directly send HTTP requests (e.g., POST requests) to AI_server endpoints using tools like Postman, cURL, or even custom scripts using Python's requests module.
Example:
1.Create a Python script (test_flask_api.py) to send data to AI_server:

        import requests
        url = 'http://127.0.0.1:5000/predict'
        data = {
           "age": 63,
           "sex": 1,
           "cp": 3,
           "trestbps": 145,
           "chol": 233,
           "fbs": 1,
           "restecg": 0,
           "thalach": 150,
           "exang": 0,
           "oldpeak": 2.3,
           "slope": 0,
           "ca": 0,
           "thal": 1
        }
        
        response = requests.post(url, json=data)
        print(response.json())  # Output the API response
2.Using cURL (Command-Line Tool)

You can use cURL from the terminal to send HTTP requests.

Steps:

Open your terminal or command prompt.

Use this command to send a POST request:

        curl -X POST http://127.0.0.1:5000/predict \
        -H "Content-Type: application/json" \
        -d '{"age": 63, "sex": 1, "cp": 3, "trestbps": 145, "chol": 233, "fbs": 1, "restecg": 0, "thalach": 150, "exang": 0, "oldpeak": 2.3, "slope": 0, "ca": 0, "thal": 1}'

The response from the AI_server will be printed in the terminal.
