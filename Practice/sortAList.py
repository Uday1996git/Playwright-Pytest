array = [13, 454, 1, 56, 7, 34, 43, 2]
z = 0

for i in range(0, len(array)):

    for j in range(i+1, len(array)):

        if array[i] > array[j]:

            z = array[i]
            array[i] = array[j]
            array[j] = z


print(array)
