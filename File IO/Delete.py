noteid ='1'
with open("notes.txt","r") as file:
    lines = file.readlines()

with open("notes.txt","w") as file:
    for x in lines:
        if not x.startswith(str(noteid) + ":"):
            file.write(x)