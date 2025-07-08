import pandas as pd

# Load the dataset
# NOTE: Update the path if your CSV is stored elsewhere
df = pd.read_csv('data/real_estate.csv')

# Show the first few entries of the transaction date column
print("Original 'X1 transaction date' values:")
print(df['X1 transaction date'].head())

# Convert transaction date to year (as integer)
# Example: "2013.250" → 2013 (year part)
df['transaction_year'] = df['X1 transaction date'].astype(str).str.split('.').str[0].astype(int)

# Optionally extract the month from the fractional part
# Multiply decimal part by 12, round and convert to month index
df['transaction_month'] = ((df['X1 transaction date'] % 1) * 12 + 1).astype(int)

# Preview the DataFrame after transformation
print("\nTransformed DataFrame with 'transaction_year' and 'transaction_month':")
print(df[['X1 transaction date', 'transaction_year', 'transaction_month']].head())

# Optional: Save the transformed DataFrame
# df.to_csv('data/real_estate_transformed.csv', index=False)
