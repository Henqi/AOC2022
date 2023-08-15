from math import copysign

rope_movement = [line.strip().split(' ') for line in open('input9.txt', 'r')]
global visited, knots
visited = []
knots = [[0,0] for i in range(10)]

def calc_movement(front, back):
    x_diff = front[0] - back[0]
    y_diff = front[1] - back[1]
    x_sign, y_sign = copysign(1, x_diff), copysign(1, y_diff)

    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return [back[0], back[1]]
    if abs(x_diff) + abs(y_diff) >= 3:
        back[0] += x_sign*1
        back[1] += y_sign*1
    else:
        if abs(x_diff) > abs(y_diff):
            back[0] += x_sign*1
        else:
            back[1] += y_sign*1

    return [back[0], back[1]]

for idx, element in enumerate(rope_movement):
    direction, steps = element[0], int(element[1])

    for step in range(steps):
        if direction == 'R':
            knots[0][0] += 1
        if direction == 'L':
            knots[0][0] -= 1
        if direction == 'U':
            knots[0][1] += 1
        if direction == 'D':
            knots[0][1] -= 1

        for knot_index, knot in enumerate(knots[:-1]):
            back_pos = calc_movement(knot, knots[knot_index+1])

        if back_pos not in visited:
            visited.append(back_pos)

RESULT = len(visited)
print('result: {RESULT}'.format(RESULT=RESULT))
