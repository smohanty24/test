import csv

# Open the CSV file
file_path = 'C:\\python-test\\risk-test.csv'
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate through rows
    for row in csv_reader:
        # Access cells by index
        cell1_value = row[0]
        cell2_value = row[1]
        # ... process the cell values as needed
        print(f"Cell 1: {cell1_value}, Cell 2: {cell2_value}")
