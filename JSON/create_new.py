import json
filename = 'student.json'
new = {"id": 3, "name": "Charlie", "age": 24, "subjects": ["Physics", "Chemistry"]}
 
#1. read file contant
with open(filename,"r") as file:
    data =json.load(file)
print(data)

#2. update json object 
data.append(new)
print(data)

#3. write json file
with open(filename,"w") as file:
    json.dump(data,file)