import string
with open('Input Day 4.txt', 'r') as file:
    passports = file.read().split('\n\n')

rules = {
    'byr' : lambda x: 1920 <= int(x) <= 2002,
    'iyr' : lambda x: 2010 <= int(x) <= 2020,
    'eyr' : lambda x: 2020 <= int(x) <= 2030,
    'hgt' : lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
    'hcl' : lambda x: len(x) == 7 and x[0] == '#' and all(c in string.hexdigits for c in x[1:]),
    'ecl' : lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid' : lambda x: len(x) == 9 and x.isnumeric(), 
    'cid' : lambda x: True
}

counter = 0
for passport in passports:
    fields = [x.split(':') for x in passport.split()]
    fieldDict = dict(fields)
    if (len(fieldDict) == 8 or (len(fieldDict) == 7 and not any('cid' in key for key in fieldDict))):
        if all(rules[key](val) for key, val in fieldDict.items()):
            counter +=1

print(counter)
