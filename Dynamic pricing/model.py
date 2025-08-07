import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("data/sample_products.csv")

# Feature Engineering
df["hour"] = pd.to_de(df["timestamp"]).dt.hour
df["is_mobile"] = datetimf["device"].apply(lambda d: 1 if d in ["Mobile", "Tablet"] else 0)

# Features and Target
X = df[["base_price", "competitor_price", "hour", "is_mobile"]]
y = df["optimal_price"]

# Train Model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "models/trained_model.pkl")

print("✅ Model trained and saved!")
