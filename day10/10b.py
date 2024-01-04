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

def right_positions(value, shift):
    if value == "|":
        if shift == (1,0):
            return [(0,-1)]
        else:
            return [(0, 1)]
        
    elif value == "-":
        if shift == (0,1):
            return [(1,0)]
        else:
            return [(-1, 0)]
        
    elif value == "F":
        if shift == (0,-1):
            return []
        else:
            return [(0,-1), (-1, 0)]
        
    elif value == "7":
        if shift == (0,1):
            return []
        else:
            return [(0,1),(-1,0)]
        
    elif value == "L":
        if shift == (1,0):
            return [(1,0), (0,-1)]
        else:
            return []
    
    elif value == "J":
        if shift == (1,0):
            return []
        else:
            return [(1,0), (0, 1)]
    

map = []

with open("10.txt", encoding = "utf-8", mode = "r") as file:
    for line in file:
        map_line = []
        for symbol in line.strip():
            map_line.append(symbol)
        map.append(map_line)

map2 = map

   
#start
for order in range(len(map)):
    
    for symbol in map[order]:
        if symbol == "S":
            S_coordinates = [order, map[order].index("S")]


coordinates = dict()
n = 0

s_coordinates = (0,0)
position_dict = { (0, -1): ["-","L", "F"], (-1, 0) : ["|","F", "7"], (1, 0): ["|","J", "L"], (0, 1):["-","J", "7"]}



#2nd step
for shift, values in position_dict.items():
    if (map[S_coordinates[0]+shift[0]][S_coordinates[1]+shift[1]]) in values:
        value = (map[S_coordinates[0]+shift[0]][S_coordinates[1]+shift[1]])
        coordinates[tuple(S_coordinates)] = shift
        new_coordinates = [S_coordinates[0]+shift[0], S_coordinates[1]+shift[1]]
        # map2[new_coordinates[0]][new_coordinates[1]] = "X"
        last_shift = shift
        n += 1
        break

s_value = False

while s_value == False:
    
    new_shift = next_shift(value, last_shift)
    coordinates[tuple(new_coordinates)] = new_shift

    value = (map[new_coordinates[0]+new_shift[0]][new_coordinates[1]+new_shift[1]])
    new_coordinates = [new_coordinates[0]+new_shift[0], new_coordinates[1]+new_shift[1]]
    # map2[new_coordinates[0]][new_coordinates[1]] = "X"
    last_shift = new_shift

    n += 1
    if value == "S":
        s_value = True

coordinates[tuple(new_coordinates)] = new_shift

print(coordinates)

for position, shift in coordinates.items():
    if map [position[0]][position[1]] != "S":
        neighb_list = right_positions(map[position[0]][position[1]], shift)
        print(position)
        if neighb_list != []:
            for a in neighb_list:
                print(a)
                col_n = position[1]+a[1]
                row_n = position[0]+a[0]
                if (col_n, row_n) not in coordinates:
                    print("yay", (col_n, row_n))         


