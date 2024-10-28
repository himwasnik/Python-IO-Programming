import csv 
employeeid = '1'
with open("employees.csv","r") as file:
    rows =[]
    for x in csv.reader(file):
        if x[0] != employeeid:
            rows.append(x)

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

