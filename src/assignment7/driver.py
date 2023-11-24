from util import print_pattern

# Take user input for the thickness
thickness = int(input("Enter thickness (must be an odd number): "))

# Call the utility function to generate and print the pattern
result = print_pattern(thickness)
for line in result:
    print(line)
