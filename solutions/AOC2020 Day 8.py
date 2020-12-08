with open('Input Day 8.txt', 'r') as file:
    instructions = [instruction.split() for instruction in file.read().split('\n')]

def run(instructions):
    acum = 0
    visited = []
    line = 0
    notCorrupted = False
    while line not in visited:
        visited.append(line)
        if line == len(instructions):
            notCorrupted = True
            break
        elif line >= len(instructions):
            break
        elif instructions[line][0] == 'acc':
            acum += int(instructions[line][1])
            line += 1
        elif instructions[line][0] == 'jmp':
            line += int(instructions[line][1])
        else:
            line += 1
    return (acum, notCorrupted)

def fixCorrupted():
    for i in range(len(instructions)):
        modInstructions = instructions
        if modInstructions[i][0] == 'jmp':  
            modInstructions[i][0] = 'nop'
        elif modInstructions[i][0] == 'nop':
            modInstructions[i][0] = 'jmp'
        acum, notCorrupted = run(modInstructions)
        if notCorrupted:
            return acum

print("Part 1:", run(instructions)[0])
print("Part 2:", fixCorrupted())