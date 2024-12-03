# Day 3 - 12/3/2024
# Mull It Over

import re

#sample input
#input="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input = open("input.txt").read()

filter = r"mul\((\d{1,3})\,(\d{1,3})\)"
filter2 = r"mul\((\d{1,3})\,(\d{1,3})\)|(don't\(\))|(do\(\))"

def runmemory(input, regex):
    total = 0
    matches = re.finditer(regex, input)
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2
    print(total)    

def runmemorypart2(input, regex):
    total = 0
    matches = re.finditer(regex, input)
    process = True
    for match in matches:
        if match.group(3):
            process = False
        elif match.group(4):
            process = True    
        else:
            if process:    
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                total += num1 * num2
    print(total)  


runmemory(input, filter)
runmemorypart2(input, filter2) 