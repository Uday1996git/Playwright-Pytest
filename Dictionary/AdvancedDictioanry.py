my_Diction = {"Java": 100, "Python": 500, "C#": 50, "Ruby": "Rails", 20: "QA", 20:"QA1"}


my_Diction["Selenium"] = 400
my_Diction["Java"] = 600

print(my_Diction)

my_Diction.pop(20)
print(my_Diction)

li = my_Diction.keys()
for i in li:
    print(i)