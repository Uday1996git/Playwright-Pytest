name = "Uday Kumar Bandaru"

my_dict = {}

for i in name:
    if i != " ":
        if my_dict.get(i.lower()):
            my_dict[i.lower()] = my_dict.get(i.lower()) + 1
        else:
            my_dict[i.lower()] = 1
print(my_dict)

for i in my_dict:
    if (my_dict[i] > 1):
        print(i + " " + str(my_dict[i]))
    else:
        print(i + " " + str(my_dict[i]))

