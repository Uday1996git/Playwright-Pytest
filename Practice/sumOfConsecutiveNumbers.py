array = [1, 3, 2, 4, 3,1, 1, 1, 1, 2, 6, 8, 3, 1]

min = 0
max = 0
diff = 0
finalVal = 0
li = []

for i in range(0, len(array)):
    current_sum = array[i]
    count = 0
    for j in range(i + 1, len(array)):
        current_sum = current_sum + array[j]
        if current_sum == 7:
            min = i
            max = j
            diff = max - min
            if diff <= finalVal or diff > 0:
                while count < diff + 1:
                    li.insert(count, array[i + count])
                    count += 1
    finalVal = diff

print(li)
