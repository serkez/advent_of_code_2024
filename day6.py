# we have an enum for directions, a counter for visited spots
# input is stores in a list of strings, sized r,c
# row, col represent the current location of the gaurd
# we automaticaal add the gaurds starting location to the counter
# then we check the direction and check the next spot assuming we are going in that direction
# if the spot is clear, we update the counter and the current location
# if its not clear, we rotate 90 ( perhaps by adding 90 to enum( if > 360, resets to 0))
# then we move that direction
# if at any point our current location is out of bounds, we have left the room and return the count
from enum import Enum

class directions(Enum):
    UP = 0
    RIGHT = 90
    DOWN = 180
    LEFT = 270
input = open("input6.txt")
grid = [x.strip() for x in input.readlines()]   
direction = directions.UP
row,col = next((row, col.index("^")) for row, col in enumerate(grid) if "^" in col)
counter = 1
visited  = []
visited.append((row,col))

def can_move(direction, row, col):
    row, col = move(direction, row, col)
    if row > -1 and row < len(grid) and col > -1 and col < len(grid[0]) and grid[row][col] != "#":
        return 1 # can move
    elif not (row > -1 and row < len(grid) and col > -1 and col < len(grid[0])):
        return 2 # out of grid
    else:
        return 0 # cant move

def move(direction, row, col):
    if direction == directions.UP:
        return row-1, col
    elif direction == directions.RIGHT:
        return row, col+1
    elif direction == directions.DOWN:
        return row+1, col
    elif direction == directions.LEFT:
        return row, col-1

def turn(direction):
    return direction.value + 90 if direction.value + 90 < 360 else 0       


while(row > -1 and row < len(grid) and col > -1 and col < len(grid[0])):
    inst = can_move(direction, row, col)
    if inst == 1:
        row, col = move(direction, row, col)
        if not (row,col) in visited:
            visited.append((row,col))
            counter += 1
    elif inst == 2:
        break    
    else:
        direction = directions(turn(direction))    
print(visited)        
print(counter)
#def move_gaurd()
