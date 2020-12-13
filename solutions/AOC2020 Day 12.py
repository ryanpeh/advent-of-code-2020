import numpy as np
with open('Input Day 12.txt', 'r') as file:
    instructions = file.read().split('\n')

move = {
    'N' : lambda x: x * np.array([0, 1]),
    'S' : lambda x: x * np.array([0, -1]),
    'E' : lambda x: x * np.array([1, 0]),
    'W' : lambda x: x * np.array([-1, 0]),
}

def part1():
    position = np.array([0, 0])
    direction = np.array([1, 0])
    for instruction in instructions:
        dire = instruction[0]
        mag = int(instruction[1:])
        if dire in ['N', 'S', 'E', 'W']:
            position += move[dire](mag)
        elif dire == 'F':
            position += direction * mag
        elif dire == 'L':
            for i in range(mag // 90):
                direction = np.array([-direction[1], direction[0]])
        elif dire == 'R':
            for i in range(mag // 90):
                direction = np.array([direction[1], -direction[0]])
    return abs(position[0]) + abs(position[1])
    
def part2():
    position = np.array([0, 0])
    direction = np.array([10, 1])
    for instruction in instructions:
        dire = instruction[0]
        mag = int(instruction[1:])
        if dire in ['N', 'S', 'E', 'W']:
            direction += move[dire](mag)
        elif dire == 'F':
            position += direction * mag
        elif dire == 'L':
            for i in range(mag // 90):
                direction = np.array([-direction[1], direction[0]])
        elif dire == 'R':
            for i in range(mag // 90):
                direction = np.array([direction[1], -direction[0]])
    return abs(position[0]) + abs(position[1])

print("Part 1:", part1())
print("Part 2:", part2())
