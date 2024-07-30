obj = open("..//Data//demo.txt", 'r')

#Read entire file
# print(obj.read())

#Read only line
# print(obj.readline())
nextLine = obj.readline()
while nextLine:
    print(nextLine)
    nextLine = obj.readline()


#To read specified number of characters from the file
# print(obj.read(10))

#To read the file character by character
#for i in obj.read():
#     print(i)


