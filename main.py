import xgboost as xgb
import pickle

# Function to load the trained model
def load_model():
    with open('xgb_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Function to predict using the model
def predict(input_data):
    model = load_model()
    prediction = model.predict(input_data)
    return prediction
