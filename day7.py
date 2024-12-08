import operator
from itertools import product

operators = {'+':operator.add, '*':operator.mul, '|':operator.concat} # remove concat for part 1
perms = {}   

lines = open('input.txt').readlines()
calibration_sum = 0

for l in lines:
    cal, nums = l.split(':')
    nums = [int(i) for i in nums.strip().split()]
    if len(nums) in perms:
        poss_cals = perms[len(nums)]
    else:
        poss_cals = list(product(['+','|','*'],repeat=len(nums)))
        perms[len(nums)] = poss_cals
    for ps in poss_cals:
        sum = nums[0]
        for i in range(1,len(nums)):
            op = operators[ps[i-1]]
            if op == operator.concat:   # remove for part 1
                sum = int(op(str(sum),str(nums[i])))
            else:
                sum = op(sum,nums[i])
        if sum == int(cal): 
            calibration_sum += sum 
            break        
print(calibration_sum)