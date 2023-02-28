import pandas as pd

# Load data from CSV file
df = pd.read_csv('retail_data.csv')

# Explore data
print(df.head())

# Clean data
df = df.drop_duplicates()
df = df.dropna()

# Analyze data
# Example: calculate total sales by product category
sales_by_category = df.groupby('category')['price'].sum()

# Generate CSV
sales_by_category.to_csv('sales_by_category.csv', index=True)
