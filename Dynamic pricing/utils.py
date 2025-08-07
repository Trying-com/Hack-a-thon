import joblib

# Load model
model = joblib.load("models/trained_model.pkl")

# Predict price
def predict_price(base_price, competitor_price, hour, device):
    is_mobile = 1 if device in ["Mobile", "Tablet"] else 0
    features = [[base_price, competitor_price, hour, is_mobile]]
    return model.predict(features)[0]
