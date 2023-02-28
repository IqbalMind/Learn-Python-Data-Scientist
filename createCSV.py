import csv

# Data to be written to the CSV file
data = [
    ['Business A', 'Product X', 10.99, 'New York'],
    ['Business B', 'Product Y', 24.99, 'Los Angeles'],
    ['Business C', 'Product Z', 5.99, 'Chicago']
]

# Open the CSV file in write mode with newline=''
with open('my_data.csv', 'w', newline='') as file:
    
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['business_name', 'product', 'price', 'location'])
    
    # Write the data rows
    for row in data:
        writer.writerow(row)
