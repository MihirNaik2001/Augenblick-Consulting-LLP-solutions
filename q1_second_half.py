def hash_algorithm(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def process_string(input_string):
    elements = input_string.split(',')
    total_sum = 0
    boxes = [[] for _ in range(256)]
    for element in elements:
        if element[len(element)-1] == '-':
            given_string = element[:-1]
            box_index = hash_algorithm(given_string)
            for sublist in boxes[box_index]:
                if sublist[0] == given_string:
                    boxes[box_index].remove(sublist)
                    break
        else:
            given_string = element[:-2]
            box_index = hash_algorithm(given_string)
            focal_length = element[-1:]
            found = False
            for sublist in boxes[box_index]:
                if sublist[0] == given_string:
                    sublist[1] = int(focal_length)
                    found = True
                    break
            if found == False:
                boxes[box_index].append([given_string,int(focal_length)])
    for i in range(256):
        if len(boxes[i]) == 0:
            continue
        j = 0
        for lable in boxes[i]:
            total_sum += (i+1)*(j+1)*lable[1]
            j += 1
            
    return total_sum

with open('input_q1.txt', 'r') as file:
    input_string = file.read()

input_string = input_string.replace('\n', '')

result = process_string(input_string)
print(result) #267372