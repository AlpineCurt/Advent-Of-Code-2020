'''https://adventofcode.com/2020/day/2'''

with open('day2_inputs.txt', 'r') as f:
    day2_list = f.readlines()

day2_inputs = list(map(str.strip, day2_list))

def day2_part1(password_test):
    '''password parameter is a string listing the min and
    max number of times a letter must appear, and the
    password.  Returns True if the required letter appears
    within the min-max number of times.'''
    
    first_split = password_test.split()
    minMax_split = first_split[0].split('-')
    
    minimum = int(minMax_split[0])
    maximum = int(minMax_split[1])
    
    key_char = first_split[1][0]
    
    password = first_split[2]
    
    key_char_count = password.count(key_char)
    
    if minimum <= key_char_count <= maximum:
        return True
    else:
        return False

valid_passwords = 0

for i in day2_inputs:
    if day2_part1(i):
        valid_passwords += 1
        
print('Part 1 Total Valid Passwords: ', valid_passwords)

###############################

def day2_part2(password_test):
    '''Parses similar to part1, but instead checks if required
    letter appears in ONLY ONE of the indices specified by min
    and max values.'''
    
    first_split = password_test.split()
    minMax_split = first_split[0].split('-')
    
    minimum = int(minMax_split[0]) - 1
    maximum = int(minMax_split[1]) - 1
    
    key_char = first_split[1][0]
    
    password = first_split[2]
    
    if (password[minimum] == key_char) ^ (password[maximum] == key_char):
        return True
    else:
        return False

valid_passwords = 0

for i in day2_inputs:
    if day2_part2(i):
        valid_passwords += 1

print('Part 2 Total Valid Passowrds: ', valid_passwords)