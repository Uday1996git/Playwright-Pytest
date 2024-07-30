

li = [12, 0, 98, 76, 45, 0, 0, 9, 0, 8, 0]


def to_end():
    count = 0
    for i in range(0, len(li)):
        if li[i] != 0:
            li[count] = li[i]
            count += 1
    while count < len(li):
        li[count] = 0
        count += 1
    return li


def to_start():
    count = len(li) - 1
    for i in range(len(li) - 1, -1, -1):
        if li[i] != 0:
            li[count] = li[i]
            count -= 1
    while count >= 0:
        li[count] = 0
        count -= 1
    return li


print(to_start())
print(to_end())
