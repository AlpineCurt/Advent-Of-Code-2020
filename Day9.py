'''https://adventofcode.com/2020/day/9'''

from itertools import combinations

def int_to_lsit(text):
    
    with open(text, 'r') as f:
        herp = f.readlines()
        
    derp = [int(x[:-1]) for x in herp]
        
    return derp  # Yeah, i'm getting sloppy.  so what?

def ruleCheck(preamble, number):
    '''Returns True if two different numbers in the preamble
    add up to number'''
    
    combos = combinations(preamble, 2)
    
    for i in list(combos):
        if sum(i) == number:
            #print(i)
            return True
    else:
        return False

def checkAll(numList, preamNum):
    '''preamNum is length of preamble'''
    
    for i, num in enumerate(numList[preamNum:]):
        preamble = numList[i:i + preamNum]
        
        if not ruleCheck(preamble, num):
            return num

def contig(numList, numSum):
    '''searches for contiguous list of numbers within numList
    that add up to numSum and returns that list'''
    
    # Slice numList to only the numbers preceeding numSum
    idx = numList.index(numSum)
    numList2 = numList[:idx]
    
    index_combos = combinations((x for x in range(idx)), 2)
    
    for i in list(index_combos):
        listCheck = numList2[i[0] : i[1]]
        if sum(listCheck) == numSum:
            return listCheck

def sumMinMax(numList):
    '''finds min and max integer in numList adds them and
    returns the result'''
    
    minimum = min(numList)
    maximum = max(numList)
    
    return minimum + maximum

#day9_test = int_to_lsit('Day9_test_inputs.txt')
#invalid = checkAll(day9_test, 5)
#contig_list = contig(day9_test, invalid)
#final_answer = sumMinMax(contig_list)


day9_inputs = int_to_lsit('Day9_inputs.txt')
invalid = checkAll(day9_inputs, 25)
contig_list = contig(day9_inputs, invalid)
final_answer = sumMinMax(contig_list)
print('Final answer: ', final_answer)