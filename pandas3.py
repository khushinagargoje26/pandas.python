
# Load the Data
# Load the sales data from a CSV file using Pandas.
import pandas as pd
import numpy as np  
df = pd.read_csv("C:\\Users\\khush\\OneDrive\\Documents\\sample2323.csv")
print("DataFrames from CSV:")
print(df)

# Clean the data by handling any missing or incorrect values
df.loc[4, 'Pincode'] = np.nan  # Introduce NaN
print("\nDataFrame with NaN value:")
print(df)

# Assume 'Pincode' column should only contain numeric values
df['Pincode'] = pd.to_numeric(df['Pincode'], errors='coerce')  # Convert non-numeric to NaN
print("\nDataFrame after correcting incorrect data types (non-numeric values to NaN in 'Pincode'):")
print(df)

# Remove rows with NaN values in 'Pincode'
df_cleaned = df.dropna(subset=['Pincode'])  # Corrected code
print("\nDataFrame after removing rows with NaN values in 'Pincode':")
print(df_cleaned)

# Optionally, remove rows where any NaN exists
df_cleaned_any_nan = df.dropna()  # Drops rows where any NaN exists
print("\nDataFrame after dropping rows with any NaN values:")
print(df_cleaned_any_nan)


# Initialize an empty dictionary to store total prices
total_prices = {}

for i, j in df.iterrows():
    product = j['Product']
    quantity = j['Quantity']
    price_each = j['price_each']
    total_price = quantity * price_each
    
    # Update total price for the product
    total_prices[product] = total_prices.get(product, 0) + total_price

# Convert the dictionary to a list of tuples
total_prices_list = [(product, price) for product, price in total_prices.items()]

# Sort the list of tuples by total price in descending order
for i in range(len(total_prices_list)):
    for j in range(i + 1, len(total_prices_list)):
        if total_prices_list[i][1] < total_prices_list[j][1]:
            total_prices_list[i], total_prices_list[j] = total_prices_list[j], total_prices_list[i]

# Print the top 5 products by total price
print("Top 5 products by total price:")
for i in range(min(5, len(total_prices_list))):
    product, price = total_prices_list[i]
    print(f"{product}: {price}")
