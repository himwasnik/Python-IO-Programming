noteid =2
updatenote = "2: Complete python assignment\n"

with open("notes.txt","r") as file:
    lines = file.readlines()

with open("notes.txt", "w") as file:
    for x in lines:
        if x.startswith(str(noteid) + ":"):
           file.write(updatenote)
        else:
            file.write(x)