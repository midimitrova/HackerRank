n = int(input())

arr = []

for i in range(n):
    commands = input().split()
    command = commands[0]

    if command == "insert":
        arr.insert(int(commands[1]), int(commands[2]))
    elif command == "print":
        print(arr)
    elif command == "remove":
        arr.remove(int(commands[1]))
    elif command == "append":
        arr.append(int(commands[1]))
    elif command == "sort":
        arr.sort()
    elif command == "pop":
        arr.pop()
    elif command == "reverse":
        arr.reverse()
