import re
with open('Input Day 7.txt', 'r') as file:
    rules = [re.split(', | contain ', x) for x in file.read().split('\n')]
bagDict = {}
holds = set()

for rule in rules:
    bags = [bag.split() for bag in rule]
    mainBag = bags[0][0] + bags[0][1]
    for bag in bags[1:]:
        if len(bag) == 4:
            if mainBag in bagDict:
                bagDict[mainBag].append((bag[0], bag[1]+bag[2]))
            else:
                bagDict[mainBag] = [(bag[0], bag[1]+bag[2])]

def hold(color):
    for curColor, contains in bagDict.items():
        if any(color == bagColors for number, bagColors in contains):
            holds.add(curColor)
            hold(curColor)

def bagsRequired(color):
    if color in bagDict:
        return sum(int(count) * bagsRequired(sub_color) for count, sub_color in bagDict[color]) + 1
    else:
        return 1

hold('shinygold')
print("Part 1:", len(holds))
print("Part 2:", bagsRequired('shinygold')-1)