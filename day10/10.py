# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def next_shift(value, shift):
    if value == "|":
        if shift == (1,0):
            return(1,0)
        else:
            return(-1,0)
    elif value == "-":
        if shift == (0,1):
            return(0, 1)
        else:
            return(0,- 1)
    elif value == "F":
        if shift == (0,-1):
            return(1,0)
        else:
            return(0,1)
    elif value == "7":
        if shift == (0,1):
            return(1,0)
        else:
            return(0,-1)
    elif value == "L":
        if shift == (1,0):
            return(0,1)
        else:
            return(-1,0)
    elif value == "F":
        if shift == (0,-1):
            return(1,0)
        else:
            return(0,1)
    elif value == "J":
        if shift == (1,0):
            return(0,-1)
        else:
            return(-1,0)
    

map = []
with open("10.txt", encoding = "utf-8", mode = "r") as file:
    for line in file:
        map.append(line.strip())

        
#start
for order in range(len(map)):
    
    for symbol in map[order]:
        if symbol == "S":
            S_coordinates = [order, map[order].index("S")]


coordinates = dict()
n = 0

s_coordinates = (0,0)
position_dict = {(0, 1):["-","J", "7"], (0, -1): ["-","L", "F"], (-1, 0) : ["|","F", "7"], (1, 0): ["|","J", "L"]}

#2nd step
for shift, values in position_dict.items():
    if (map[S_coordinates[0]+shift[0]][S_coordinates[1]+shift[1]]) in values:
        value = (map[S_coordinates[0]+shift[0]][S_coordinates[1]+shift[1]])
        new_coordinates = [S_coordinates[0]+shift[0], S_coordinates[1]+shift[1]]
        last_shift = shift
        n += 1
        break

s_value = False

while s_value == False:
  
    new_shift = next_shift(value, last_shift)
    value = (map[new_coordinates[0]+new_shift[0]][new_coordinates[1]+new_shift[1]])
    new_coordinates = [new_coordinates[0]+new_shift[0], new_coordinates[1]+new_shift[1]]
    last_shift = new_shift
    n += 1
    if value == "S":
        s_value = True

print(n/2)
        
         














            