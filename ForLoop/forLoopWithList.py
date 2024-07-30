li = [10, "Uday", 30, "Kumar"]
z = 0
for i in li:
    # print(i)
    if str(i).isalpha():
        print(i)
    elif str(i).isdigit():
        z = z + i

print(z)