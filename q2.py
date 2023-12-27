with open('input_q2.txt', 'r') as file:
    input_string = file.read()

input_array = input_string.split('\n')

num_rows = len(input_array)
num_cols = len(input_array[0])

result = 0

for col in range(num_cols):
    upmost_index = 0
    for row in range(num_rows):
        if input_array[row][col] == 'O':
            result += (num_rows - upmost_index)
            upmost_index += 1
        elif input_array[row][col] == '#':
            upmost_index = row + 1

print(result)