from copy import deepcopy
with open('Input Day 11.txt', 'r') as file:
    seats = list(map(list,file.read().split('\n')))

rows = len(seats)
columns = len(seats[0])

def adjOccupied(seats, row, column):
    occupied = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= row+i < rows and 0 <= column+j < columns and not (i == j == 0):
                if seats[row+i][column+j] == '#':
                    occupied += 1
    return occupied

def part1(seats):
    prev = deepcopy(seats)
    count = 0
    for i in range(rows):
        for j in range(columns):
            if prev[i][j] == 'L':
                if adjOccupied(prev, i, j) == 0:
                    seats[i][j] = '#'
                    count += 1
            elif prev[i][j] == '#':
                if adjOccupied(prev, i, j) >= 4:
                    seats[i][j] = 'L'
                else: count += 1
    if prev == seats:
        return count
    return part1(seats)


def longOccupied(seats, row, column):
    occupied = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(1, max(rows, columns)):
                if 0 <= row+k*i < rows and 0 <= column+k*j < columns and not (i == j == 0):
                    if seats[row+k*i][column+k*j] == '#':
                        occupied += 1
                        break
                    elif seats[row+k*i][column+k*j] == 'L':
                        break
    return occupied

def part2(seats):
    prev = deepcopy(seats)
    count = 0
    for i in range(rows):
        for j in range(columns):
            if prev[i][j] == 'L':
                if longOccupied(prev, i, j) == 0:
                    seats[i][j] = '#'
                    count += 1
            elif prev[i][j] == '#':
                if longOccupied(prev, i, j) >= 5:
                    seats[i][j] = 'L'
                else: count += 1
    if prev == seats:
        return count
    return part2(seats)

print("Part 1:", part1(seats))
print("Part 2:", part2(seats))