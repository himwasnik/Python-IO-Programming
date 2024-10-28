import json

studentid = 1
newname = "himanshu"

with open("student.json","r") as file:
    finaldata = json.load(file)

#update
for student in finaldata:
    if student["id"] == studentid:
        student["name"] = newname
        break

with open("student.json", "w") as file:
    json.dump(finaldata, file)
