# Historian Hysteria: part 1
# 12/1/2024

# goal : take n lines of input, for each line, get 2 numbers split on " "
# create 1 list with all the numbers on the right, and one for the left
# sort the lists
# calculate the difference between the values in both lists for all i
# add that value to a variable
# print the variable
# point, finding the difference between the smallest number in each list for each smallest numebr

input = open("day1/day1_input.txt", "r")
lines = input.readlines()
list1 = []
list2 = []
for line in lines:
    splited = line.split("   ")
    list1.append(int(splited[0]))
    list2.append(int(splited[1]))
list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)        



# Historian Hysteria: part 2
# 12/1/2024

# goal : take n lines of input, for each line, get 2 numbers split on " "
# create 1 list with all the numbers on the right, and one for the left
# find the number of time each value in 1 appears in 2
# multiply the number of times it appears by the value, add to variable
# print the variable
# use dictionaries to store the values and their counts

input = open("day1/day1_input.txt", "r")
lines = input.readlines()
list1 = []
dict = {}
for line in lines:
    splited = line.split("   ")
    num1 = int(splited[0])
    num2 = int(splited[1])
    list1.append(num1)
    if num2 not in dict:
        dict[num2] = 1
    else:
        dict[num2] += 1


total = 0
for i in range(len(list1)):
    if list1[i] in dict:
        total += list1[i] * dict[list1[i]]

print(total)        
