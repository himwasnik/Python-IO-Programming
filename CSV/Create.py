import csv

new_employee = [3, "Sam Brown", "Marketing", 55000]

with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_employee)
