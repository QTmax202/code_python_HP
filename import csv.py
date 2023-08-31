import csv
# Create a list of data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Mary', 25, 'Boston'],
    ['Bob', 40, 'Chicago']
]
# Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the data to the CSV file
    csvwriter.writerows(data)