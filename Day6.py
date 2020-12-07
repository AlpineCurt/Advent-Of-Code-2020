'''https://adventofcode.com/2020/day/6'''

input_text_test = 'Day6_test_inputs.txt'
input_text = 'Day6_inputs.txt'

def openFormatInput(text):
    '''read input text and remove newlines'''

    with open(text, 'r') as f:
        day6_text = f.read()
    
    day6_list = day6_text.split('\n\n')
    
    day6_list2 = []
    
    for i in day6_list:
        i = i.replace('\n', '')
        day6_list2.append(i)
    
    return day6_list2

def uniqueChars(response):
    '''response is a string.  This counts the numnber
    of unique character occurances and returns the total.'''
    
    seen = set()
    unique_chars = 0
    for i in response:
        if i not in seen:
            seen.add(i)
            unique_chars += 1
    
    return unique_chars

def totalYeses(answers):
    '''answers is a list of strings'''
    
    total_yeses = 0
    for i in answers:
        total_yeses += uniqueChars(i)    
    
    return total_yeses


test_group_answers = openFormatInput(input_text_test)
#group_answers = openFormatInput(input_text)
total_yeses = totalYeses(test_group_answers)

print('Part 1 Total yeses: ', total_yeses)



### Part 2 ###

def openFormatInput_Part2(text):
    '''read input text and remove newlines'''

    with open(text, 'r') as f:
        day6_text = f.read()
    
    day6_list = day6_text.split('\n\n')
    
    group_answers_split = []
    for i in day6_list:
        group_answers_split.append(i.split('\n'))    
    
    return group_answers_split

group_answers = openFormatInput_Part2(input_text)
test_group_answers = openFormatInput_Part2(input_text_test)

def find_same_chars(char_list):
    '''char_list is a list of strings.  This returns the number of
    characters that appear in every list'''
    
    persons_in_group = len(char_list)
    matching_char_count = 0
    total_match_chars = 0
    
    for letter in char_list[0]:
        matching_char_count = 0
        for answers in char_list:
            if letter in answers:
                matching_char_count += 1
        else:
            if matching_char_count == len(char_list):
                total_match_chars += 1
    
    return total_match_chars
    

def totalYesespart2(answers):
    '''answers is a list of strings'''
    
    total_yeses = 0
    for i in answers:
        total_yeses += find_same_chars(i)    
    
    return total_yeses    

#print(test_group_answers)
print('Sun of questions where everyone answered yes: ', totalYesespart2(group_answers))



