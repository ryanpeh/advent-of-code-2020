with open('Input Day 10.txt', 'r') as file:
    input = list(map(int, file.read().split('\n')))

def part1(adapters):
    prev = oneDiff = threeDiff = 0
    for adapter in sorted(adapters):
        if adapter - prev == 1: oneDiff += 1
        elif adapter - prev == 3: threeDiff += 1
        prev = adapter
    return oneDiff * (threeDiff + 1)

def part2(adapters):
    adapters.sort()
    counter = [1] + [0] * max(adapters)
    for adapter in adapters:
        counter[adapter] = counter[adapter-1] + counter[adapter-2] + counter[adapter-3]
    return counter[-1]

## Part 2 using recursion and memoization instead of dp
memo = {}
def routes(adapters, prev):
    if prev <= adapters[0] <= prev + 3:
        if (len(adapters) == 1):
            return 1
        elif ((adapters[0], prev) in memo):
            return memo[(adapters[0], prev)]
        else:
            memo[(adapters[0], prev)] = routes(adapters[1:], prev) + routes(adapters[1:], adapters[0])
            return memo[(adapters[0], prev)]
    else:
        return 0
    
print("Part 1:", part1(input))
print("Part 2:", part2(input))
#print("Part 2:", routes(sorted(input), 0))
