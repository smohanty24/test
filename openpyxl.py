import openpyxl
from openpyxl import Workbook
# Load the Excel file
file_path = 'C:\python-test\risk-test.xlsx'
workbook = openpyxl.load_workbook(file_path)

# Select a specific sheet
sheet = workbook['Sheet1']  # Replace 'Sheet1' with your sheet name

# Iterate through rows and columns
for row in sheet.iter_rows(min_row=2, values_only=True):  # Start from the second row (assuming headers in the first row)
    col1_value = row[0]
    col2_value = row[1]
    # ... process the values as needed
    print(f"Column 1: {col1_value}, Column 2: {col2_value}")

# Close the workbook when done
workbook.close()
