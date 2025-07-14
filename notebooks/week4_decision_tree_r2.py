# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("/mnt/data/Real estate.csv")

# Drop the 'No' column if it exists (it's just an index)
if 'No' in df.columns:
    df = df.drop(columns=['No'])

# Define features and target
X = df.drop("Y house price of unit area", axis=1)
y = df["Y house price of unit area"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train the Decision Tree Regressor
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate using R² score
r2 = r2_score(y_test, y_pred)
print("Decision Tree R² Score:", r2)
