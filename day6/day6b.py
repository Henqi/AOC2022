with open('input6.txt', 'r') as file:
    char_list = list(file.read())

def is_unique_chars(input):
    input_list = list(input)
    input_set = set(input)
    input_set_tolist = list(input_set)
    
    input_list.sort()
    input_set_tolist.sort()
    
    return input_list == input_set_tolist

for i in range(0, len(char_list)):
    if is_unique_chars(char_list[i:i+14]):
        print('result index:' + str(i+14))
        break