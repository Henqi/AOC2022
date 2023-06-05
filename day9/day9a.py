from math import copysign

rope_movement = [line.strip().split(' ') for line in open('input9.txt', 'r')]
visited = []
head_location, tail_location = [0, 0], [0, 0]

def calc_tail_location():
    x_diff = head_location[0] - tail_location[0]
    y_diff = head_location[1] - tail_location[1]
    x_sign, y_sign = copysign(1, x_diff), copysign(1, y_diff)

    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return
    if abs(x_diff) + abs(y_diff) == 3:
        tail_location[0] += x_sign*1
        tail_location[1] += y_sign*1    
    else:
        if abs(x_diff) > abs(y_diff):
            tail_location[0] += x_sign*1
        else:
            tail_location[1] += y_sign*1

    visited.append([tail_location[0], tail_location[1]])

for idx, element in enumerate(rope_movement):
    direction, steps = element[0], int(element[1])

    for step in range(steps):
        if direction == 'R':
            head_location[0] += 1
        if direction == 'L':
            head_location[0] -= 1
        if direction == 'U':
            head_location[1] += 1
        if direction == 'D':
            head_location[1] -= 1
        calc_tail_location()

RESULT = set([str(location) for location in visited])
print('result: {RESULT}'.format(RESULT=len(RESULT)))
