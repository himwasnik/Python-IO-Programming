import csv

employid = '2'
newsalary = '70000'

with open("employees.csv","r") as file:
    rows =list(csv.reader(file))

for x in rows:
    if x[0] == employid:
        x[3] = newsalary

with open("employees.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)