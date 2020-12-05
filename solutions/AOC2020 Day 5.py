with open('Input Day 5.txt', 'r') as file:
    input = file.read().split('\n')

def seatIDs(passList):
    return [int(boardingPass.replace('L', '0').replace('R', '1').replace('F', '0').replace('B', '1'), 2) for boardingPass in passList]
IDList = sorted(seatIDs(input))

print("Part 1:", max(IDList))
print("Part 2:", [x for x in range(min(IDList), max(IDList)+1) if x not in IDList][0])

