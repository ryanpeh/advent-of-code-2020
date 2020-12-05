with open('Input Day 1.txt', 'r') as file:
    input = [int(x) for x in file.readlines()]
for i in input:
    if (2020-i) in input:
        print(i*(2020-i))
        break
for i in input:
    for j in input:
        if (2020-i-j) in numbers:
            print(i*j*(2020-i-j))
            break