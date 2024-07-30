Number = 1346899999
newNumber = 0
my_Dict = {}

# while int(Number) != 0:
#     newNumber = newNumber*10+int(Number)%10
#     Number = Number /10
# print(newNumber)

while int(Number) != 0:
    if int(Number) % 10 in my_Dict:
        my_Dict[int(Number) % 10] = my_Dict.get(int(Number) % 10) + 1
    else:
        my_Dict[int(Number) % 10] = 1

    Number = Number / 10
print(my_Dict)

for i in my_Dict.keys():
    if my_Dict.get(i) > 1:
        print(i)
