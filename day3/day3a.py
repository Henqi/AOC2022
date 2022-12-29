import string

with open('input3.txt', 'r') as file:
    inventory = file.read().split('\n')

items = list(string.ascii_letters)
priorities = list(range(1,53))

values = {}
points = 0

for key, value in zip(items, priorities):
    values[key] = value

for rucksack in inventory:
    first_bag = rucksack[:int(len(rucksack)/2)]
    second_bag = rucksack[int(len(rucksack)/2):]

    common_item = ''.join(set(first_bag).intersection(second_bag))
    points += values[common_item]

print(points)
