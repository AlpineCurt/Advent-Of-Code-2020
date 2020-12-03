'''https://adventofcode.com/2020/day/3'''

with open('day3_inputs.txt', 'r') as f:
    day3_list = f.readlines()

day3_inputs = list(map(str.strip, day3_list))

def tree_repeat(tree_patterns):
    '''This will take tree_patterns and extend each item in
    the list by repeating the pattern and return the resulting
    list.'''
    
    minLen = len(tree_patterns) * 7  # moving 3 to the right for every item
    
    repeating_pattern = []
    
    for i in tree_patterns:
        pattern = i
        while len(pattern) < minLen:
            pattern += pattern
        repeating_pattern.append(pattern)
    
    return repeating_pattern

def tree_hit_count(tree_pattern, right, down):
    '''Starting at index 0 of first item in tree_pattern, this checks
    if you encounter a tree (#) or not (.)  This then checks "right"
    indices ahead in the next item and so on, tallying the total trees
    encountered and returns the result.'''
    
    tree_hits = 0
    slope_index = 0
    right_adv = right
    down_adv = down
    
    for i, pattern in enumerate(tree_pattern):
        if i % down_adv != 0:
            continue
        if pattern[slope_index] == '#':
            tree_hits += 1
        slope_index += right_adv
    
    return tree_hits

#### Part 1 ####

day3_tree_pattern = tree_repeat(day3_inputs)
day3_tree_hit_total = tree_hit_count(day3_tree_pattern, 3, 1)
print('Total Trees Hit: ', day3_tree_hit_total)

#### Part 2 ####

r1d1 = tree_hit_count(day3_tree_pattern, 1, 1)
r3d1 = tree_hit_count(day3_tree_pattern, 3, 1)
r5d1 = tree_hit_count(day3_tree_pattern, 5, 1)
r7d1 = tree_hit_count(day3_tree_pattern, 7, 1)
r1d2 = tree_hit_count(day3_tree_pattern, 1, 2)

day3_part2_answer = r1d1 * r3d1 * r5d1 * r7d1 * r1d2

print('Total trees: ', day3_part2_answer)
