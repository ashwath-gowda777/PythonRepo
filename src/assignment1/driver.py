from util import process_commands

N = int(input("Enter the number of commands: "))
user_commands = [input().split() for i in range(N)]
process_commands(user_commands)