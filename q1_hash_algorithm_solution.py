def hash_algorithm(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def calculate_sum(input_string):
    elements = input_string.split(',')
    total_sum = sum(hash_algorithm(value) for value in elements)
    return total_sum

with open('input_q1.txt', 'r') as file:
    input_string = file.read()

input_string = input_string.replace('\n', '')

result = calculate_sum(input_string)
print("The sum of the HASH algorithm values is:", result) #517965