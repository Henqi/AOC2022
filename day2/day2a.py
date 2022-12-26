# ME
# X for Rock
# Y for Paper
# Z for Scissors

# OPPONENT
# A for Rock
# B for Paper
# C for Scissors

with open('input2.txt', 'r') as file:
    strategy = file.read().split('\n')

strategy = [x.replace(' ', '') for x in strategy]

shape_points = {'X':1, 'Y':2, 'Z':3} # points for playing shape
my_wins = ['CX', 'AY', 'BZ'] # win = 6 points
draws = ['AX', 'BY', 'CZ'] # draw = 3 points

points = 0

for round in strategy:
    for key in shape_points:
        if key in round:
            points += shape_points[key]
    if round in my_wins:
        points += 6
    if round in draws:
        points += 3

print(points)