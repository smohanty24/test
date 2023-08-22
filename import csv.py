import csv
import encodings
import re
import itertools

# Open the CSV file
file_path = 'C:\\python-test\\risk-test.csv'
csv_file_path = "C:\\python-test\\output1.csv"

high_risk_issues = []
medium_risk_issues = []
low_risk_issues = []
issues = {}
issuesdist_high={}
issuesdist_medium={}
issuesdist_low={}

issuesummary={}


# Adding key-value pairs
#empty_dict["key1"] = "value1"
#empty_dict["key2"] = "value2"


with open(file_path,  errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file)
    high_risk_count=0
    medium_risk_count=0
    low_risk_count=0
    pattern1 = re.compile(r'High')
    pattern2 = re.compile(r'Medium')
    pattern3 = re.compile(r'Low')

    # Iterate through rows
    for row in csv_reader:
        
        # Access cells by index
        cell1_value = row[0]
        cell2_value = row[1]
        cell3_value = row[2]
        cell4_value = row[3]
        if pattern1.match(cell2_value):
             high_risk_count=high_risk_count+1 
             #risks=cell1_value .split(":")
             temp_string=cell1_value+"-"+cell4_value;
             issuesdist_high[cell1_value]=cell4_value
             high_risk_issues.append(temp_string)     
        if pattern2.match(cell2_value):
             medium_risk_count=medium_risk_count+1
             #risks=cell1_value .split(":")
             medium_risk_issues.append(cell1_value)
             issuesdist_medium[cell1_value]=cell4_value
             
        if pattern3.match(cell2_value):
             low_risk_count=low_risk_count+1
             #risks=cell1_value .split(":")
             low_risk_issues.append(cell1_value)
             issuesdist_low[cell1_value]=cell4_value
               
issues["high"]= high_risk_issues

issues["medium"]= medium_risk_issues
issues["Low"]= low_risk_issues

            
        # ... process the cell values as needed
print(f"IssueName: {cell1_value}, RiskLevel: {cell2_value},Criticality: {cell3_value}, Number: {cell4_value}")

print(f"Hish Risk Issues: {high_risk_count},Medium Risk Issues: {medium_risk_count},Low Risk Issues: {low_risk_count}")

print("=======High==========")
print(f"Count : {high_risk_count}")
print(high_risk_issues)


print("=======Medium==========")
print(f"Count : {medium_risk_count}")
print(medium_risk_issues)

issuesummary['high']=issuesdist_high
issuesummary['high_cnt']=high_risk_count

issuesummary['medium']=issuesdist_medium
issuesummary['medium_cnt']=medium_risk_count

issuesummary['low']=issuesdist_low
issuesummary['low_cnt']=low_risk_count


print("=======Low==========")
print(f"Count : {low_risk_count}")
print(low_risk_issues)
print(issuesdist_high)

print("FInal issues=============")
print(issuesummary)

fields = [ 'Risk', 'Level', 'Type', 'Count' ]
with open("csv_file_path", "wb") as f:
    w = csv.DictWriter(f, fields)
    w.writeheader()
    for k in issuesummary:
        w.writerow({field: issuesummary[k].get(field) or k for field in fields})
