'''https://adventofcode.com/2020/day/8'''

def getdata(text):
    '''Parses a text file and returns a list for every line.'''
    
    with open(text, 'r') as f:
        opList = f.readlines()
    
    # Remove newline char
    for i, op in enumerate(opList):
        opList[i] = op[:-1]
    
    # split into a tuple
    operations = []
    for op in opList:
        operations.append(op.split())
    
    # convert numbers to integers
    for i, op in enumerate(operations):
        operations[i][1] = int(op[1])
    
    return operations

def findLoop(ops):
    '''Follows each instruction in ops and tracks the
    accumulator.  When an instruction is attempted a
    second time, returns the accumulator value'''
    
    accum = 0 # accumulator value
    idx = 0 # index of instruction
    completed = set()
    
    while True:
        if idx in completed:
            print('Loop hit.  Accumulator = ', accum)
            return False
        elif idx + 1 > len(ops):
            print('Program Complete.  Accumulator = ', accum)
            return accum
        
        completed.add(idx)
        
        
        if ops[idx][0] == 'acc':
            accum += ops[idx][1]
            idx += 1
        elif ops[idx][0] == 'jmp':
            idx += ops[idx][1]
        elif ops[idx][0] == 'nop':
            idx += 1
        else:
            print('Bad ops instruction')

def fixCode(ops):
    '''ops is a list of instructions'''
    
    for i in range(len(ops)):
        
        testOps = list(ops)
        
        if testOps[i][0] == 'nop':
            testOps[i][0] = 'jmp'
        elif testOps[i][0] == 'jmp':
            testOps[i][0] = 'nop'
        else:
            continue
        
        if not findLoop(testOps):
            # Change it back
            if testOps[i][0] == 'nop':
                testOps[i][0] = 'jmp'
            elif testOps[i][0] == 'jmp':
                testOps[i][0] = 'nop'            
            continue
        else:
            break 
            

#day8_test = getdata('Day8_test_inputs.txt')
day8_input = getdata('Day8_inputs.txt')
#findLoop(day8_input)
#fixCode(day8_test)
fixCode(day8_input)