input = open("input.txt").readlines()
numword1 = 0
numword2 = 0
count = 0

def find_word(i, j, count)->int:
    count = 0
    #if j + 3 < len(input[i]):
    # right
    count += 1 if j + 3 < len(input[i]) and input[i][j + 1] == "M" and input[i][j + 2] == "A" and input[i][j + 3] == "S" else 0
    # left
    count += 1 if j - 3 >= 0 and input[i][j - 1] == "M" and input[i][j - 2] == "A" and input[i][j - 3] == "S" else 0
    # up
    count += 1 if i - 3 >= 0 and input[i - 1][j] == "M" and input[i - 2][j] == "A" and input[i - 3][j] == "S" else 0
    # down    
    count += 1 if i + 3 < len(input) and input[i + 1][j] == "M" and input[i + 2][j] == "A" and input[i + 3][j] == "S" else 0    
    # diagonal right down
    count += 1 if i + 3 < len(input) and j + 3 < len(input[i]) and input[i + 1][j + 1] == "M" and input[i + 2][j + 2] == "A" and input[i + 3][j + 3] == "S" else 0
    # diagonal left down
    count += 1 if i + 3 < len(input) and j - 3 >= 0 and input[i + 1][j - 1] == "M" and input[i + 2][j - 2] == "A" and input[i + 3][j - 3] == "S" else 0
    # diagonal right up
    count += 1 if i - 3 >= 0 and j + 3 <= len(input[i]) and input[i - 1][j + 1] == "M" and input[i - 2][j + 2] == "A" and input[i - 3][j + 3] == "S" else 0
    # diagonal left up
    count += 1 if i - 3 >= 0 and j - 3 >= 0 and input[i - 1][j - 1] == "M" and input[i - 2][j - 2] == "A" and input[i - 3][j - 3] == "S" else 0
    return count


def find_x(i,j)->int:
    if i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(input) and j + 1 < len(input[i]):
        if input[i-1][j-1]=="M" and input[i+1][j+1]=="S" or input[i-1][j-1]=="S" and input[i+1][j+1]=="M":
            if input[i-1][j+1]=="M" and input[i+1][j-1]=="S" or input[i-1][j+1]=="S" and input[i+1][j-1]=="M":
                return 1
    return 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "X":
            numword1 += find_word(i, j, count)
        if input[i][j] == "A": # for part two, start from "A"s and check if they are in the center of an X 
            numword2 += find_x(i,j)
print(numword1)  
print(numword2)          