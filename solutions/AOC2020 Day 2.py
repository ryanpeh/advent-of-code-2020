with open('Input Day 2.txt', 'r') as file:
    inputs = file.readlines()

counter1 = 0
counter2 = 0
for input in inputs:
    counts, letter, password = input.split()
    least, most = counts.split('-')
    if int(least) <= password.count(letter[0]) <= int(most):
        counter1 += 1
    if ((password[int(least)-1] == letter[0]) != (password[int(most)-1] == letter[0])):
        counter2 += 1

print("Part 1: " + str(counter1))
print("Part 2: " + str(counter2))