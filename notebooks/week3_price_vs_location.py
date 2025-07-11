import pandas as pd
import matplotlib.pyplot as plt

# Load and preprocess the dataset
df = pd.read_csv("/mnt/data/Real estate.csv")

# Rename relevant columns for clarity
df = df.rename(columns={
    'X5 latitude': 'latitude',
    'X6 longitude': 'longitude',
    'Y house price of unit area': 'price_per_unit_area'
})

# Create scatter plot: Price distribution by location
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['longitude'], df['latitude'], 
                      c=df['price_per_unit_area'], cmap='viridis', 
                      edgecolor='k', alpha=0.7)
plt.colorbar(scatter, label='Price per Unit Area')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Price Distribution by Location")
plt.grid(True)
plt.tight_layout()
plt.show()
