with open('Input Day 15.txt', 'r') as file:
    input = list(map(int,file.read().split(',')))

def elf(number):
    mem = {}
    for a, b in enumerate(input, 1):
        mem[b] = a
        cur = b
    mem.pop(cur)
    for count in range(len(input), number):
        if cur not in mem:
            mem[cur] = count
            cur = 0
        else:
            next = count - mem[cur]
            mem[cur] = count
            cur = next
    return cur

print('Part 1:', elf(2020))
print('Part 2:', elf(30000000))
