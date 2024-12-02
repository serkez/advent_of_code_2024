def valid(levels) -> bool:
    increasing = True if levels[0] < levels[1] else False
    if increasing:
        for i in range(1, len(levels)):
            if levels[i] - levels[i-1] <= 0 or levels[i] - levels[i-1] > 3:
                return False
    else:
        for i in range(0, len(levels)-1):
            if levels[i] - levels[i+1] <= 0 or levels[i] - levels[i+1] > 3:
                return False   
    return True

def subsets(arr) -> list:
        subsets = []
        for i in range(len(arr)):
            sub = arr[:i] + arr[i+1:]
            subsets.append(sub)
        return subsets    



# 12/1/2024
# Day 2: Red-Nosed Reports
# part 1


input = open("input.txt", "r")
lines = input.readlines()
num_safe = 0
levels = []
for line in lines:
    levels = list(map(int,line.split(" ")))
    if valid(levels):
            num_safe += 1
print(num_safe)    

# Day 2: Red-Nosed Reports
# part 2

input = open("input.txt", "r")
lines = input.readlines()
num_safe = 0
levels = []
for line in lines:
    levels = list(map(int,line.split(" ")))
    if valid(levels):
            num_safe += 1
    else:
        allsubs = subsets(levels)
        for sub in allsubs:
            if valid(sub):
                num_safe += 1
                break  
print(num_safe)                  