from itertools import combinations

with open('Input Day 9.txt', 'r') as file:
    numbers =  list(map(int, file.read().split('\n')))

def invalidNumber(): 
    for i in range(25, len(numbers)):
        pairSum = [sum(x) for x in combinations(numbers[(i-25):i], 2)]
        if numbers[i] not in pairSum:
            return(numbers[i])

def encryptionWeakness(invalidNumber):
    for i in range(len(numbers)):
        acum = []
        for j in range(i, len(numbers)):
            acum.append(numbers[j])
            if sum(acum) == invalidNumber:
                return min(acum) + max(acum)
            elif sum(acum) > invalidNumber:
                break

print("Part 1:", invalidNumber())
print("Part 2:", encryptionWeakness(invalidNumber()))