import json
import csv
import os

class Employee:
    def __init__(self, name, age, department, email, phone_number):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phone_number = phone_number

    # Save employee details to various files
    def save_to_files(self):
        # Append to TXT file
        with open("employees.txt", "a") as txt_file:
            txt_file.write(f"{self.name},{self.age},{self.department},{self.email},{self.phone_number}\n")
        
        # Append to JSON file
        employee_record = {
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "email": self.email,
            "phone_number": self.phone_number
        }
        if os.path.exists("employees.json"):
            with open("employees.json", "r") as json_file:
                data = json.load(json_file)
                data.append(employee_record)
        else:
            data = [employee_record]
        
        with open("employees.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        # Append to CSV file
        file_exists = os.path.isfile("employees.csv")
        with open("employees.csv", "a", newline="") as csv_file:
            fieldnames = ["name", "age", "department", "email", "phone_number"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(employee_record)

    # Display employee data from TXT
    @staticmethod
    def display_from_txt():
        with open("employees.txt", "r") as txt_file:
            for line in txt_file:
                print(line.strip())

    # Display employee data from CSV
    @staticmethod
    def display_from_csv():
        with open("employees.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)

    # Display employee data from JSON
    @staticmethod
    def display_from_json():
        with open("employees.json", "r") as json_file:
            data = json.load(json_file)
            for entry in data:
                print(entry)

    # Update existing employee data in all files
    @staticmethod
    def update_employee_record(old_name, new_employee):
        # Update TXT file
        with open("employees.txt", "r") as txt_file:
            lines = txt_file.readlines()
        
        with open("employees.txt", "w") as txt_file:
            for line in lines:
                if line.startswith(old_name + ","):
                    txt_file.write(f"{new_employee.name},{new_employee.age},{new_employee.department},{new_employee.email},{new_employee.phone_number}\n")
                else:
                    txt_file.write(line)
        
        # Update JSON file
        with open("employees.json", "r") as json_file:
            data = json.load(json_file)
        
        for entry in data:
            if entry["name"] == old_name:
                entry.update(vars(new_employee))
        
        with open("employees.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        # Update CSV file
        with open("employees.csv", "r") as csv_file:
            rows = list(csv.reader(csv_file))
        
        with open("employees.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for row in rows:
                if row[0] == old_name:
                    writer.writerow([new_employee.name, new_employee.age, new_employee.department, new_employee.email, new_employee.phone_number])
                else:
                    writer.writerow(row)

    # Remove employee record from all files
    @staticmethod
    def remove_employee(name):
        # Remove from TXT file
        with open("employees.txt", "r") as txt_file:
            lines = txt_file.readlines()
        
        with open("employees.txt", "w") as txt_file:
            for line in lines:
                if not line.startswith(name + ","):
                    txt_file.write(line)
        
        # Remove from JSON file
        with open("employees.json", "r") as json_file:
            data = json.load(json_file)
        
        data = [entry for entry in data if entry["name"] != name]
        
        with open("employees.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        # Remove from CSV file
        with open("employees.csv", "r") as csv_file:
            rows = list(csv.reader(csv_file))
        
        with open("employees.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for row in rows:
                if row[0] != name:
                    writer.writerow(row)

def gather_employee_info():
    name = input("Name: ")
    age = int(input("Age: "))
    department = input("Department (e.g., IT, HR): ")
    email = input("Email: ")
    phone_number = input("Phone number: ")

    return Employee(name, age, department, email, phone_number)

def main():
    while True:
        print("\n*** Employee Management System ***")
        print("1. Add Employee")
        print("2. Display Employees (TXT)")
        print("3. Display Employees (CSV)")
        print("4. Display Employees (JSON)")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("7. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            new_employee = gather_employee_info()
            new_employee.save_to_files()
        elif choice == "2":
            Employee.display_from_txt()
        elif choice == "3":
            Employee.display_from_csv()
        elif choice == "4":
            Employee.display_from_json()
        elif choice == "5":
            existing_name = input("Enter name of employee to update: ")
            updated_employee = gather_employee_info()
            Employee.update_employee_record(existing_name, updated_employee)
        elif choice == "6":
            name_to_remove = input("Enter name of employee to delete: ")
            Employee.remove_employee(name_to_remove)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
