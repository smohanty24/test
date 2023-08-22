import csv

# Dictionary of data
data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"},
    {"name": "Alice", "age": 28, "city": "Chicago"}
]

# Specify the CSV file path
csv_file_path = "C:\\python-test\\output.csv"

# Write the dictionary data to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write header row
    for row in data:
        writer.writerow(row)
