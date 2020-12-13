with open('Input Day 13.txt', 'r') as file:
    input = file.read().split('\n')

buses = [(x,int(y)) for x, y in enumerate(input[1].split(',')) if y != 'x']

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a>1 :
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0 : x1 += b0
    return x1

def part1():
    leave = int(input[0])
    while True:
        for _, bus in buses:
            if leave % bus == 0:
                return bus * (leave - int(input[0]))
        leave += 1
    return 0

def part2():
    prod, res = 1, 0
    for rem, num in buses:
        prod *= num
    for rem, num in buses:
        pp = prod // num
        res += -rem * mul_inv(pp, num) * pp
    return res % prod
    
print("Part 1:", part1())
print("Part 2:", part2())