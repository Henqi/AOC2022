# ME
# X for Rock
# Y for Paper
# Z for Scissors

# OPPONENT
# A for Rock
# B for Paper
# C for Scissors

# ROUND2
# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win

with open('input2.txt', 'r') as file:
    strategy = file.read().split('\n')

strategy = [x.replace(' ', '') for x in strategy]

result_points = {'X':0, 'Y':3, 'Z':6} # points when playing with predetermined outcome
shape_points = {'X':1, 'Y':2, 'Z':3} # points for playing shape

lose = {'A':'Z', 'B':'X', 'C':'Y'}
draw = {'A':'X', 'B':'Y', 'C':'Z'}
win = {'A':'Y', 'B':'Z', 'C':'X'}

points = 0

for round in strategy:
    for key in result_points:
        if key in round:
            points += result_points[key]

            if key == 'X':
                points += shape_points[lose[round[0]]]
            elif key == 'Y':
                points += shape_points[draw[round[0]]]
            elif key == 'Z':
                points += shape_points[win[round[0]]]
                
print(points)