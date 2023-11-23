#1
def list_operations(commands):
    l1 = []

    for com in commands:
        if com[0] == "insert":
            l1.insert(int(com[1]),int(com[2]))
        elif com[0] == "print":
            print(l1)
        elif com[0] == "remove":
            e = int(com[1])
            l1.remove(e)
        elif com[0] == "append":
            e = int(com[1])
            l1.append(e)
        elif com[0] == "sort":
            l1.sort()
        elif com[0] == "pop":
            l1.pop()
        elif com[0] == "reverse":
            l1 = l1[::-1]

    return l1  # Return the modified list




