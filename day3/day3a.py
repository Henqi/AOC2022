import string

with open('input3.txt', 'r') as file:
    inventory = file.read().split('\n')

item_types = list(string.ascii_letters)
priorities = list(range(1,53))

item_priorities = {}

for key, value in zip(item_types, priorities):
    item_priorities[key] = value

sum_of_prio = 0

for rucksack in inventory:
    first_bag = rucksack[:int(len(rucksack)/2)]
    second_bag = rucksack[int(len(rucksack)/2):]

    common_item = ''.join(set(first_bag).intersection(second_bag))
    sum_of_prio += item_priorities[common_item]

print(sum_of_prio)
