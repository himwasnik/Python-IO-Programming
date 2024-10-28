import json

with open("student.json", "r") as file:
    finaldata = json.load(file)

# for particular id
for x in finaldata:
    print(x['subjects'][1])
