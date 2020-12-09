'''https://adventofcode.com/2020/day/7'''

class BagRules():
    
    def __init__(self, ruleText):
        '''ruleText is the text file containing the rules.'''
        
        self.ruleDict = self.createRules(ruleText)
        
        self.found = False
        self.bagCount = 0
    
    def createRules(self, ruleText):
        '''Parses ruleText and returns a dict of key, values
        of bagColor, list of bagColors it can contain'''
        
        with open(ruleText, 'r') as f:
            ruleList = f.readlines()
        
        ruleList2 = []
        for rule in ruleList:
            ruleList2.append(rule.split(' bags contain '))
        
        # Remove Newline from each
        for i, rule in enumerate(ruleList2):
            if rule[1][-1:] == '\n':
                ruleList2[i][1] = rule[1][:-2]
        
        # Convert to Dictionary
        ruleList3 = {}
        for rule in ruleList2:
            ruleList3[rule[0]] = rule[1].split(', ')
        
        # Remove 'bag(s)'from each item
        for rule in ruleList3:
            for i, bag in enumerate(ruleList3[rule]):
                if 'bags' in bag:
                    ruleList3[rule][i] = bag[:-5]
                elif 'bag' in bag:
                    ruleList3[rule][i] = bag[:-4]
        
        # create lists of number of contained bags
        ruleList4 = {}
        for rule in ruleList3:
            if ruleList3[rule][0][0] == 'n':
                ruleList4[rule] = []
                continue
            bagList = []
            for i, bag in enumerate(ruleList3[rule]):
                numColor = []
                numColor.append(int(bag[0]))
                numColor.append(ruleList3[rule][i][2:])
                bagList.append(numColor)
            ruleList4[rule] = bagList
        
        return ruleList4
    
    def searchBag(self, bagColor, searchColor):
        '''Is searchColor eventually found in bagColor?  If it's found,
        self.found is set to True.'''
        
        if self.found:
            return
        for bag in self.ruleDict[bagColor]:
            if self.found:
                break
            if searchColor in bag:
                self.found = True
        else:
            for bag in self.ruleDict[bagColor]:
                if self.found:
                    break
                self.searchBag(bag[1], searchColor)        
        
    def countBagsContainingColor(self, searchColor):
        '''Checks every bag in self.ruleDict to see if searchColor
        can be stored in the bag directly or indirectly (bag within
        bag within bag etc).  Returns the total number of bags that
        can hold searchColor.'''
        
        goodbags = 0
        for bag in self.ruleDict.keys():
            self.found = False
            self.searchBag(bag, searchColor)
            if self.found:
                goodbags += 1
        return goodbags
    
    def bagception(self, bagColor):
        '''Adds to self.bagCount the total number of bags within bagColor'''
        
        if len(self.ruleDict[bagColor]) == 0:
            return
        
        for bag in self.ruleDict[bagColor]:
            if len(self.ruleDict[bag[1]]) == 0:
                self.bagCount += bag[0]
            else:
                self.bagCount += bag[0]
                for i in range(bag[0]):
                    self.bagception(bag[1])

Day7 = BagRules('Day7_inputs.txt')
print('Number of bags that can contain at least one shiny gold bag:, ', Day7.countBagsContainingColor('shiny gold'))
Day7.bagception('shiny gold')
print('Num of bags inside one shiny gold: ', Day7.bagCount)
