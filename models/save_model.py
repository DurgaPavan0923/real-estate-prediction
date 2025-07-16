import joblib
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import os

df = pd.read_csv("../data/folder/cleaned_data_with_transaction_year.csv")

x = df.drop("price_per_unit_area", axis=1)
y = df["price_per_unit_area"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = XGBRegressor(random_state=42)
model.fit(x_train, y_train)

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/final_model.pkl")