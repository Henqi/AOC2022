with open('input8.txt', 'r') as file:
    tree_map = [line.strip() for line in file.readlines()]

SCENIC_SCORE_LIST = []

def calc_scenic_score(tree_x, tree_y, tree_height):
    score_west, score_east, score_north, score_south = 0, 0, 0, 0

    for position in range(tree_x - 1, -1, -1): #west
        if int(tree_map[tree_y][position]) >= tree_height:
            score_west += 1
            break
        else:
            score_west += 1

    for position in range(tree_x + 1, len(tree_map[0])): #east
        if int(tree_map[tree_y][position]) >= tree_height:
            score_east += 1
            break
        else:
            score_east += 1

    for position in range(tree_y - 1 , -1, -1): #north
        if int(tree_map[position][tree_x]) >= tree_height:
            score_north += 1
            break
        else:
            score_north += 1

    for position in range(tree_y + 1, len(tree_map)): #south
        if int(tree_map[position][tree_x]) >= tree_height:
            score_south += 1
            break
        else:
            score_south += 1

    SCENIC_SCORE_LIST.append(score_west*score_east*score_north*score_south)

for y in range(len(tree_map)):
    for x in range(len(tree_map[0])):
        calc_scenic_score(x, y, int(tree_map[y][x]))

RESULT = max(SCENIC_SCORE_LIST)
print('result: {RESULT}'.format(RESULT=RESULT))
