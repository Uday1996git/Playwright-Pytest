import functools


def sort_Characters(string):
    char = " "
    li = list(string)
    for i in range(0, len(li)):
        for j in range(i + 1, len(li)):
            if li[i].lower() > li[j].lower():
                # print(li[i])
                char = li[j].lower()
                li[j] = li[i].lower()
                li[i] = char
    return li


string = "Uday"
# for i in range(0, len(string)):
#     if string[i]> 'v':
#
#         print(string[i])
print(sort_Characters(string))

#Converting a list to String using reduce method from functools module
str1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(functools.reduce(lambda x, y: x + y, list(str1)))
