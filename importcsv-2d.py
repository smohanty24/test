import csv

# Nested dictionary
data = {
    "person1": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
}

# Specify the CSV file path
csv_file_path = "C:\\python-test\\output2.csv"

# Write the nested dictionary to the CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    fieldnames = ["person_id", "name", "age", "city"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write header row
    for person_id, person_data in data.items():
        row = {"person_id": person_id, **person_data}
        writer.writerow(row)
