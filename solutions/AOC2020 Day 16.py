
with open('Input Day 16.txt', 'r') as file:
    fields, myTicket, nearbyTickets = file.read().split('\n\n')

numbers = {}
myTicket = (myTicket.split('\n'))[1].split(',')
nearbyTickets = [i.split(',') for i in (nearbyTickets.split('\n'))[1:]]

for field in fields.split('\n'):
    word, val = field.split(': ')
    left, right = val.split(' or ')
    a1, a2 = left.split('-')
    b1, b2 = right.split('-')
    numbers[word] = [int(a1), int(a2), int(b1), int(b2)]

errorRate = 0

for ticket in nearbyTickets:
    for val in ticket:
        errorRate += int(val)
        for a1, a2, b1, b2 in numbers.values():
            if (a1 <= int(val) <= a2 or b1 <= int(val) <= b2):
                errorRate -= int(val)
                break

possibleFields = {}

for i in range(len(myTicket)):
    possibleFields[i] = set([i for i in numbers.keys()])

for ticket in nearbyTickets:
    for position, val in enumerate(ticket):
        for field, nums in numbers.items():
            a1, a2, b1, b2 = nums
            if not (a1 <= int(val) <= a2 or b1 <= int(val) <= b2):
                possibleFields[position].discard(field)
                    
acum = 1

for i, fields in possibleFields.items():
    for field in fields:
        if field[:9] == 'departure':
            acum *= int(myTicket[i])
            break


print(acum)
