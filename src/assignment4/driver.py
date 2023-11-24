from src.assignment4.util import mutate_string

if __name__ == '__main__':
    input_string = input("Enter the initial string: ")
    mutation_position = int(input("Enter the mutation position: "))
    mutation_character = input("Enter the mutation character: ")

    mutated_result = mutate_string(input_string, mutation_position, mutation_character)

    print("Custom Function Result:", mutated_result)
   

