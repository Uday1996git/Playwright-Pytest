name = "Uday Kumar Bandaru"
s = " "
# i = len(name)-1
count = 0
for i in range(len(name)-1, -1, -1):
    if count == 0:
        s = s+name[i].capitalize()
        count+=1
    elif name[i] == " ":
        count = 0
        s = s + name[i].lower()
    else:
        s = s + name[i].lower()
print(s)