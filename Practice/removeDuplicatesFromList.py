li = [13, 12, 3, 4, 13, 4, 78, 78]
li2 = []
li1 = []
count = 0
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i] == li[j]:
            li1.insert(count, j)
            count += 1

print(li1)
count = 0

for j in range(0, len(li)):
    if j in li1:
        continue
    else:
        li2.insert(count, li[j])
        count += 1
        # print(li2)

print(li2)
