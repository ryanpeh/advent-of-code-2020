import itertools
with open('Input Day 14.txt', 'r') as file:
    input = [x.split(' = ') for x in file.read().split('\n')]


def part1():
    mem = {}
    for instruction, val in input:
        if instruction == 'mask':
            mask = val
        else:
            binary = f"{int(val):036b}"
            idx = instruction[4:-1]
            overwrite = ''
            for a, b in zip(binary, mask):
                if b == 'X':
                    overwrite += a
                else:
                    overwrite += b
            mem[idx] = int(overwrite, 2)
    return sum(mem.values())

def part2():
    mem = {}
    for instruction, val in input:
        if instruction == 'mask':
            mask = val
        else:
            binary = f"{int(instruction[4:-1]):036b}"
            overwrite = ''
            for a, b in zip(binary, mask):
                if b == '0':
                    overwrite += a
                else:
                    overwrite += b
            xIdx = [i for i, x in enumerate(overwrite) if x == 'X']
            bitPerms = list(itertools.product('01', repeat=len(xIdx)))
            for i in bitPerms:
                temp = overwrite
                for c, idx in enumerate(xIdx):
                    temp = temp[:idx] + i[c] + temp[idx+1:]
                mem[temp] = int(val)
    return sum(mem.values())

print("Part 1:", part1())
print("Part 2:", part2())