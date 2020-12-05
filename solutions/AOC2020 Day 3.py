with open('Input Day 3.txt', 'r') as file:
    map = file.read().split('\n')
width = len(map[0])
height = len(map)

def traverse(right, down):
    counter = curX = curY = 0
    while (curY < height):
        if map[curY][curX%width] == '#':
            counter += 1
        curX += right
        curY += down
    return counter

# Part 1
print(traverse(3,1))
# Part 2
print(traverse(1,1)*traverse(3,1)*traverse(5,1)*traverse(7,1)*traverse(1,2))

