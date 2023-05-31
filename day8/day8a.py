with open('input8.txt', 'r') as file:
    tree_map = [line.strip() for line in file.readlines()]

visible_trees = []

def check_visibility_west(tree_x, tree_y, tree_height):
    for position in range(tree_x):
        if int(tree_map[tree_y][position]) >= tree_height:
            return False
    visible_trees.append('')
    return True

def check_visibility_east(tree_x, tree_y, tree_height):
    for position in range(tree_x + 1, len(tree_map[0])):
        if int(tree_map[tree_y][position]) >= tree_height:
            return False
    visible_trees.append('')
    return True

def check_visibility_north(tree_x, tree_y, tree_height):
    for position in range(tree_y):
        if int(tree_map[position][tree_x]) >= tree_height:
            return False
    visible_trees.append('')
    return True

def check_visibility_south(tree_x, tree_y, tree_height):
    for position in range(tree_y + 1, len(tree_map)): 
        if int(tree_map[position][tree_x]) >= tree_height:
            return False
    visible_trees.append('')
    return True

def check_visibility(tree_x, tree_y, tree_height):
    west = check_visibility_west(tree_x, tree_y, tree_height)
    if west == True:
        return
    east = check_visibility_east(tree_x, tree_y, tree_height)
    if east == True:
        return
    north = check_visibility_north(tree_x, tree_y, tree_height)
    if north == True:
        return
    south = check_visibility_south(tree_x, tree_y, tree_height)
    if south == True:
        return

for y in range(len(tree_map)):
    for x in range(len(tree_map[0])):
        if x == 0 or y == 0:
            visible_trees.append('')
            continue
        if x == len(tree_map[0])-1 or y == len(tree_map)-1:
            visible_trees.append('')
            continue
            
        check_visibility(x, y, int(tree_map[y][x]))


result = len(visible_trees)
print('result: {result}'.format(result=result))