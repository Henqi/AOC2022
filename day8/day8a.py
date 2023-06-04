with open('input8.txt', 'r') as file:
    tree_map = [line.strip() for line in file.readlines()]

VISIBLE_TREES = 0

def check_visibility(tree_x, tree_y, tree_height):
    global VISIBLE_TREES

    for position in range(tree_x): #west
        if int(tree_map[tree_y][position]) >= tree_height:
            break
        if position == tree_x-1:
            VISIBLE_TREES += 1
            return
    
    for position in range(tree_x + 1, len(tree_map[0])): #east
        if int(tree_map[tree_y][position]) >= tree_height:
            break
        if position == len(tree_map[0])-1:
            VISIBLE_TREES += 1
            return

    for position in range(tree_y): #north
        if int(tree_map[position][tree_x]) >= tree_height:
            break
        if position == tree_y-1:
            VISIBLE_TREES += 1
            return

    for position in range(tree_y + 1, len(tree_map)): #south
        if int(tree_map[position][tree_x]) >= tree_height:
            break
        if position == len(tree_map)-1:
            VISIBLE_TREES += 1
            return

for y in range(len(tree_map)):
    for x in range(len(tree_map[0])):
        if x == 0 or y == 0:
            VISIBLE_TREES += 1
            continue
        if x == len(tree_map[0])-1 or y == len(tree_map)-1:
            VISIBLE_TREES += 1
            continue
        check_visibility(x, y, int(tree_map[y][x]))

RESULT = VISIBLE_TREES
print('result: {RESULT}'.format(RESULT=RESULT))
