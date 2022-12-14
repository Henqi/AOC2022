
with open('input1.txt', 'r') as file:
    data = file.read().split('\n\n')

max_calories = 0

for elf in data:
    elf = elf.split('\n')
    max = sum([int(x) for x in elf])
    if max > max_calories:
        max_calories = max
    
print(max_calories)
