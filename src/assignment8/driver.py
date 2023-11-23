from util import day_name

if __name__ == '__main__':
    month, day, year = map(int, input("Enter month, day, and year (separated by space): ").split())
    result = day_name(month, day, year)
    print("The day is: " + result)

