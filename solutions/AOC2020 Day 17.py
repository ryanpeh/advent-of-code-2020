import itertools
with open('Input Day 17.txt', 'r') as file:
    input = file.read().split('\n')

cubeGrid = set()
for y, row in enumerate(input):
    for x, cube in enumerate(row):
        if cube == '#':
            cubeGrid.add((x, y, 0, 0))

def part1(cycles, cubeGrid):
    if cycles == 0: return len(cubeGrid)
    nextGrid = set()
    for x, y, z in list(itertools.product(range(min(min(i) for i in cubeGrid) - 1, max(max(i) for i in cubeGrid) + 2), repeat=3)):
        adj = 0
        for i, j, k in list(itertools.product([-1, 0, 1], repeat=3)):
            if (x + i, y + j, z + k, 0) in cubeGrid:
                adj += 1
        if ((x, y, z, 0) in cubeGrid and adj in (3,4)) or ((x, y, z, 0) not in cubeGrid and adj == 3):
            nextGrid.add((x+1, y+1, z+1, 0))
    return(part1(cycles-1, nextGrid))

def part2(cycles, cubeGrid):
    if cycles == 0: return len(cubeGrid)
    nextGrid = set()
    for x, y, z, w in list(itertools.product(range(min(min(i) for i in cubeGrid) - 1, max(max(i) for i in cubeGrid) + 2), repeat=4)):
        adj = 0
        for i, j, k, l in list(itertools.product([-1, 0, 1], repeat=4)):
            if (x + i, y + j, z + k, w + l) in cubeGrid:
                adj += 1
        if ((x, y, z, w) in cubeGrid and adj in (3,4)) or ((x, y, z, w) not in cubeGrid and adj == 3):
            nextGrid.add((x+1, y+1, z+1, w+1))
    return(part2(cycles-1, nextGrid))

print("Part 1:", part1(6, cubeGrid))
print("Part 2:", part2(6, cubeGrid))