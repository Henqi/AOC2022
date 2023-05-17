with open('input5.txt', 'r') as file:
    instructions = file.read().split('\n')[10:]

# first item/index on the bottom of stack
stack1 = ['D', 'L', 'V', 'T', 'M', 'H', 'F']
stack2 = ['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P']
stack3 = ['R', 'S', 'D', 'M', 'P', 'H']
stack4 = ['L', 'B', 'V', 'F']
stack5 = ['N', 'H', 'G', 'L', 'Q']
stack6 = ['W', 'B', 'D', 'G', 'R', 'M', 'P']
stack7 = ['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q']
stack8 = ['C', 'L', 'W']
stack9 = ['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T']
all_stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

split_instructions = [line.split(' ') for line in instructions]

def execute_instructions(instructions):
    move_amount = int(instructions[1])
    from_stack_index = int(instructions[3])-1
    from_stack = all_stacks[from_stack_index]
    to_stack = all_stacks[int(instructions[5])-1]

    moving_boxes = from_stack[-move_amount:]
    #moving_boxes.reverse() # crane can now lift multiple boxes simultaneously
    all_stacks[from_stack_index] = from_stack[:-move_amount]
    to_stack.extend(moving_boxes)

[execute_instructions(line) for line in split_instructions]

result = [stack[-1] for stack in all_stacks]
print('result: ' + ''.join(result))