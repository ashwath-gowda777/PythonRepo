from util import list_operations

N = int(input("Enter the number of commands: "))
user_commands = [input().split() for i in range(N)]
list_operations(user_commands)
