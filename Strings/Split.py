name = "Uday Kumar Bandaru"

result = name.split(" ")
print(len(result))
print(result)

for i in result:
    for j in i:
        if j == "d":
            print(j)