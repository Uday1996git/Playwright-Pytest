
s = {"Uday": 1}
k = ["Uday"]
if s.keys().__contains__("Uday"):
    print("Yes")
print(s.get("Uday"))
s["Uday"] = s.get("Uday")+1
print(s["Uday"])

s["Kumar"] = 2

print(s)
print(k[0])
k.insert(1, "Kumar")
print(k)
k[1] = 'Bandaru'
print(k)

print(s.keys())