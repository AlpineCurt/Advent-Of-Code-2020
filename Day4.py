'''https://adventofcode.com/2020/day/4'''

with open('day4_inputs.txt', 'r') as f:
    day4_text = f.read()

def text_to_dicts(text):
    '''Parses text and returns a list of dicts.'''

    day4_list = text.split('\n\n')
    
    day4_list2 = []
    
    for i in day4_list:
        
        bob = []  # temp list's name is bob
        
        first_split = i.split('\n')
        
        for n in first_split:
            if ' ' not in n:
                bob.append(n)
            else:
                bob.extend(n.split())
        
        day4_list2.append(bob)
    
    if len(day4_list) != len(day4_list2):
        print('Error parsing lists:  output list not same length as input.')
    
    del day4_list2[-1][-1]
    
    passports = []
    
    for i in day4_list2:
        bob2 = {}  # temp dict's name is bob
        for n in i:
            key, val = n.split(':')
            bob2[key] = val
        passports.append(bob2)
    
    return passports

def valid_passport(passport):
    '''passport parameter is a dict.  A passport is valid if it has eight unique
    keys.  If it has seven and key 'cid' is missing, still returns True.'''
    
    if len(passport) == 8:
        return True
    elif len(passport) == 7 and 'cid' not in passport:
        return True
    else:
        return False

passports = text_to_dicts(day4_text)

valids = 0
for i in passports:
    if valid_passport(i):
        valids += 1

print('Part 1 Total Valid Passports: ', valids)

#### Part 2 ####

def valid_passport_part2(passport):
    '''passport parameter is a dict.  A passport is valid if it has eight unique
    keys.  If it has seven and key 'cid' is missing, still returns True.'''
    
    if len(passport) <= 6:
        return False
    if len(passport) == 7 and 'cid' in passport:
        return False
    
    if len(passport['byr']) != 4:
        return False
    try:
        byr = int(passport['byr'])
    except:
        return False
    if byr < 1920 or byr > 2002:
        return False
    
    if len(passport['iyr']) != 4:
        return False    
    try:
        iyr = int(passport['iyr'])
    except:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    
    if len(passport['eyr']) != 4:
        return False    
    try:
        eyr = int(passport['eyr'])
    except:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    
    if passport['hgt'][-2:] != 'cm' and passport['hgt'][-2:] != 'in':
        return False
    try:
        if passport['hgt'][-2:] == 'cm':
            hgt = int(passport['hgt'][0:3])
            if hgt < 150 or hgt > 193:
                return False
        elif passport['hgt'][-2:] == 'in':
            hgt = int(passport['hgt'][0:2])
            if hgt < 59 or hgt > 76:
                return False
    except:
        return False
    
    if passport['hcl'][0] != '#':
        return False
    if len(passport['hcl']) != 7:
        return False
    valid_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
                   'b', 'c', 'd', 'e', 'f'}
    for char in passport['hcl'][1:]:
        if char not in valid_chars:
            return False
    
    valid_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if passport['ecl'] not in valid_ecl:
        return False
    
    if len(passport['pid']) != 9:
        return False
    try:
        int(passport['pid'])
    except:
        return False
    
    return True

valids = 0
for i in passports:
    if valid_passport_part2(i):
        valids += 1

print('Part 2 Total Valid Passports: ', valids)