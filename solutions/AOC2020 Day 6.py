with open('Input Day 6.txt', 'r') as file:
    answers = [group.split() for group in file.read().split('\n\n')]

anyoneAnswer = everyoneAnswer = 0

for answer in answers:
    answer = list(map(set,answer))
    anyoneAnswer += len(set.union(*answer))
    everyoneAnswer += len(set.intersection(*answer))

print("Part 1:", anyoneAnswer)
print("Part 2:", everyoneAnswer)