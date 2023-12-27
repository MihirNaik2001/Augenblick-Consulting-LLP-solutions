import json

def apply_cycle(input_array):

    result_array = input_array
    num_rows = len(input_array)
    num_cols = len(input_array[0])
    for col in range(num_cols):
        upmost_index = 0
        for row in range(num_rows):
            if result_array[row][col] == 'O':
                result_array[upmost_index][col] = 'O'
                if upmost_index != row:
                  result_array[row][col] = '.'
                upmost_index += 1
            elif result_array[row][col] == '#':
                upmost_index = row + 1

    for row in range(num_rows):
        leftmost_index = 0
        for col in range(num_cols):
            if result_array[row][col] == 'O':
                result_array[row][leftmost_index] = 'O'
                if leftmost_index != col:
                    result_array[row][col] = '.'
                leftmost_index += 1
            elif result_array[row][col] == '#':
                leftmost_index = col + 1
    
    for col in range(num_cols):
        downmost_index = num_rows - 1
        for row in range(num_rows-1,-1,-1):
            if result_array[row][col] == 'O':
                result_array[downmost_index][col] = 'O'
                if downmost_index != row:
                    result_array[row][col] = '.'
                downmost_index -= 1
            elif result_array[row][col] == '#':
                downmost_index = row - 1

    for row in range(num_rows):
        rightmost_index = num_cols - 1
        for col in range(num_cols-1,-1,-1):
            if result_array[row][col] == 'O':
                result_array[row][rightmost_index] = 'O'
                if rightmost_index != col:
                    result_array[row][col] = '.'
                rightmost_index -= 1
            elif result_array[row][col] == '#':
                rightmost_index = col - 1
    
    return result_array

with open('input_q2.txt', 'r') as file:
    input_string = file.read()

input_array = input_string.split('\n')
input_array = [list(string) for string in input_array]

result = 0

num_rows = len(input_array)
num_cols = len(input_array[0])

seen_states = {}

for i in range(1000000000):
    input_array = apply_cycle(input_array)
    state = json.dumps(input_array)
    if state in seen_states:
        cycle_start = seen_states[state]
        cycle_length = i - cycle_start
        remaining_cycles = 1000000000 - i
        cycle_offset = remaining_cycles % cycle_length

        for _ in range(cycle_offset - 1):
            input_array = apply_cycle(input_array)
        break
    seen_states[state] = i

for row in range(num_rows):
    for col in range(num_cols):
        if input_array[row][col] == 'O':
            result += (num_rows - row)

print(result)#103861