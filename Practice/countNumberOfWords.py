
s = "May may might maybe mist"

s1 = s.split(" ")
s2 ={}

for i in range(0, len(s1)):
    for j in range(i, len(s1)):
        if s1[i].lower() == s1[j].lower():
            print(s1[i])
            if s2.keys().__contains__(s1[i].lower()):
                if s2.get(s1[i].lower()):
                    s2[s1[i].lower()] = s2.get(s1[i].lower()) + 1
            else:
                s2[s1[i].lower()] = 1
print(s2)
