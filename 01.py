import csv
import json
import os

class Employee:
    def __init__(self, name, age, department, email, phone_number):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phone_number = phone_number

    # write file of txt, csv, json
    def write_to_file(self):
        # Ensure directory exists
        os.makedirs("task", exist_ok=True)

        with open("task/employee.txt", 'a') as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Age: {self.age}\n")
            f.write(f"Department: {self.department}\n")
            f.write(f"Email: {self.email}\n")
            f.write(f"Phone_Number: {self.phone_number}\n")
            f.write("\n")

        # csv write
        with open("task/employee.csv", "a", newline='') as file:
            data = csv.writer(file)
            data.writerow([self.name, self.age, self.department, self.email, self.phone_number])

        # json write
        try:
            with open("task/employee.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "email": self.email,
            "phone_number": self.phone_number
        })

        with open("task/employee.json", 'w') as f2:
            json.dump(data, f2, indent=4)

    # read txt file
    @staticmethod
    def read_text_file():
        with open("task/employee.txt", 'r') as f:
            data = f.read()
            print(data)

    # read csv file
    @staticmethod
    def read_csv_file():
        with open("task/employee.csv", 'r') as f:
            data = csv.reader(f)
            for line in data:
                print(line)

    # read json file
    @staticmethod
    def read_json_file():
        with open("task/employee.json", 'r') as f:
            data = json.load(f)
            for users in data:
                print(users)

    # Update data
    @staticmethod
    def update_data(old, new):
        # Update text file
        with open("task/employee.txt", 'r') as f:
            lines = f.readlines()
        with open("task/employee.txt", 'w') as f2:
            for line in lines:
                f2.write(line.replace(old, new))

        # Update CSV file
        with open("task/employee.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
        with open("task/employee.csv", 'w', newline='') as f2:
            writer = csv.writer(f2)
            for row in rows:
                updated_row = []
                for word in row:
                    if word == old:
                        updated_row.append(new)
                    else:
                        updated_row.append(word)
                writer.writerow(updated_row)

        # Update JSON file
        with open("task/employee.json", "r") as file:
            data = json.load(file)
            for entry in data:
                for key in entry:
                    if entry[key] == old:
                        entry[key] = new
        with open("task/employee.json", "w") as f2:
            json.dump(data, f2, indent=4)

    # delete operation
    @staticmethod
    def delete_items(name):
        # Remove from JSON file
        with open("task/employee.json", "r") as json_file:
            data = json.load(json_file)
        data = [entry for entry in data if entry["name"] != name]
        with open("task/employee.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
            
        # Remove from CSV file
        with open("task/employee.csv", "r") as csv_file:
            rows = list(csv.reader(csv_file))
        
        with open("task/employee.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for row in rows:
                if row[0] != name:
                    writer.writerow(row)

        # Remove from TXT file
        with open("task/employee.txt", "r") as txt_file:
            lines = txt_file.readlines()
        
        with open("task/employee.txt", "w") as txt_file:
            for line in lines:
                if not line.startswith(f"Name: {name}"):
                    txt_file.write(line)

# Menu function
def menu():
    while True:
        print("\n1. Add Employee\n2. Read Employees from txt\n3. Read Employees from CSV\n4. Read Employees from JSON\n5. Update Employee\n6. Delete Employee\n7. Exit")

        choice = input("Enter choice no: ")
    
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            department = input("Enter department (HR, IT, Finance): ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")

            emp = Employee(name, age, department, email, phone_number)
            emp.write_to_file()

        elif choice == '2':
            Employee.read_text_file()

        elif choice == '3':
            Employee.read_csv_file()

        elif choice == '4':
            Employee.read_json_file()

        elif choice == '5':
            old = input("Enter old value to change: ")
            new = input("Enter new value to change: ")
            Employee.update_data(old, new)

        elif choice == '6':
            name = input("Enter name you want to delete: ")
            Employee.delete_items(name)

        elif choice == '7':
            break
        else:
            print("Enter valid operation.")

menu()
