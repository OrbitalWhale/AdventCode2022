with open('calories.txt') as f:
        lines = f.readlines()
elf_calories_carried = []
numbers = []
for x in lines:
    if x != '\n':
        x.strip()
        numbers.append(x.strip())
    elif x == '\n':
        elf_calories_carried.append(sum(map(int, numbers)))
        numbers = []
max_calorie = max(elf_calories_carried)
index = elf_calories_carried.index(max_calorie) + 1
print("Elf " + str(index) + " has the most calories with a total of " + str(max_calorie))

top3 = sorted(elf_calories_carried, reverse=True)[:3]
print(sum(top3))