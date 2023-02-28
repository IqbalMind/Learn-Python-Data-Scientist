import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV file
df = pd.read_csv('retail_data.csv')

# Data preprocessing
df = df.drop_duplicates()
df = df.dropna()

# Feature engineering
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['weekday'] = df['date'].dt.weekday

# Customer segmentation
customer_segments = pd.DataFrame({'customer_id': df['customer_id'].unique()})
customer_segments['total_spent'] = df.groupby('customer_id')['price'].sum().values
customer_segments['num_purchases'] = df.groupby('customer_id')['product'].count().values
customer_segments['avg_order_value'] = customer_segments['total_spent'] / customer_segments['num_purchases']
customer_segments['segment'] = pd.cut(customer_segments['total_spent'], bins=[0, 100, 500, 1000, np.inf], labels=['Low', 'Medium', 'High', 'Very high'])
customer_segments.to_csv('customer_segments.csv', index=False)

# Sales analysis
sales_by_category = df.groupby('category')['price'].sum()
sales_by_month = df.groupby(['year', 'month'])['price'].sum().reset_index()
sales_by_month['month'] = sales_by_month['month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
sales_by_weekday = df.groupby('weekday')['price'].sum()
sales_by_hour = df.groupby(df['date'].dt.hour)['price'].sum()

# Data visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values, palette='rocket')
plt.title('Sales by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='month', y='price', data=sales_by_month, hue='year', palette='viridis')
plt.title('Monthly Sales Trends', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_weekday.index, y=sales_by_weekday.values, palette='magma')
plt.title('Sales by Weekday', fontsize=14)
plt.xlabel('Weekday', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x=sales_by_hour.index, y=sales_by_hour.values, color='purple')
plt.title('Hourly Sales Trends', fontsize=14)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.tight_layout()
plt.show()
