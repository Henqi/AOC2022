import string

with open('input3.txt', 'r') as file:
    n = 3
    data = [line.strip() for line in file.readlines()]
data = [data[i:i + n] for i in range(0, len(data), n)]

items = list(string.ascii_letters)
priorities = list(range(1,53))

values = {}

for key, value in zip(items, priorities):
    values[key] = value

points = 0

for rucksack in data:
    common_item = ''.join(set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2]))
    points += values[common_item]

print(points)