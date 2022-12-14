
with open('input1.txt', 'r') as file:
    data = file.read().split('\n\n')

calories = []

for elf in data:
    elf = elf.split('\n')
    elf = [int(x) for x in elf]
    calories.append(sum(elf))

print(sum(sorted(calories)[-3:]))
