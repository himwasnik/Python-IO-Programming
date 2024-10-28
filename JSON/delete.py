import json
studentid =3

with open("student.json","r") as file:
    data = json.load(file)

data = [student for student in data if student["id"] != studentid]

with open("student.json","w") as delete:
    json.dump(data,delete)


