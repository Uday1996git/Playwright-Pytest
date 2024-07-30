count = 0
current_sum = 0
for i in range(1, 100):
    # if count == 10:
    #     break
    current_sum = current_sum + i
    count += 1
else:
    print("Loop ended")
print(current_sum)