'''https://adventofcode.com/2020/day/5'''

from math import ceil

with open('day5_inputs.txt', 'r') as f:
    day5_list = f.readlines()

day5_inputs = list(map(str.strip, day5_list))

def findSeatRowCol(seat):
    '''Returns a tuple of (row, column)'''
    
    #print(seat[:7])
    
    row_high = 127
    row_low = 0
    
    for row in seat[:7]:
        diff = ceil((row_high - row_low) / 2)
        if row.upper() == 'F':
            row_high -= diff
        elif row.upper() == 'B':
            row_low += diff
    
    if row_low != row_high:
        print('Row High and Low values do not match!')
        print('Row low: ', row_low)
        print('Row high: ', row_high)
    
    col_high = 7
    col_low = 0
    
    for col in seat[7:]:
        diff = ceil((col_high - col_low) / 2)
        if col.upper() == 'L':
            col_high -= diff
        elif col.upper() == 'R':
            col_low += diff
    
    if col_low != col_high:
        print('Col High and Low values do not match!')
        print('Col low: ', col_low)
        print('Col high: ', col_high)
    
    return (row_low, col_low)

def calcSeatID(rowCol):
    '''rowCol is a tuple with two integers'''
    
    return (rowCol[0] * 8) + rowCol[1]

allSeatIDs = set()
for seat in day5_inputs:
    rowCol = findSeatRowCol(seat)
    seatID = calcSeatID(rowCol)
    allSeatIDs.add(seatID)

print('Highest Seat ID: ', max(allSeatIDs))

for i in range(850):
    if i not in allSeatIDs:
        if i - 1 in allSeatIDs and i + 1 in allSeatIDs:
            print('Empty seat at: ', i)