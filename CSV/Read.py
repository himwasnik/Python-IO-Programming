import csv

with open("employees.csv","r") as file:
    data = csv.reader(file)
    for x in data:
        print(x)
