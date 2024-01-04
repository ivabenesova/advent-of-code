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
            return [(0,-1), (-1, 0)]
        else:
            return []
        
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
position_dict = {  (0, 1):["-","J", "7"], (0, -1): ["-","L", "F"], (-1, 0) : ["|","F", "7"], (1, 0): ["|","J", "L"] }



# 2nd step
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
    coordinates[tuple(new_coordinates)] = last_shift

    value = (map[new_coordinates[0]+new_shift[0]][new_coordinates[1]+new_shift[1]])
    new_coordinates = [new_coordinates[0]+new_shift[0], new_coordinates[1]+new_shift[1]]
    # map2[new_coordinates[0]][new_coordinates[1]] = "X"
    last_shift = new_shift

    n += 1
    if value == "S":
        s_value = True

coordinates[tuple(new_coordinates)] = new_shift


keys = []
right = []

for key in coordinates.keys():  
    keys.append(key)
print(3)
for position, shift in coordinates.items():
    if map[position[0]][position[1]] != "S":
        neighb_list = right_positions(map[position[0]][position[1]], shift)
        if neighb_list != []:
            for a in neighb_list:
                col_n = position[0]+a[0]
                row_n = position[1]+a[1]
                
                if (col_n, row_n) not in keys :
                    if (col_n, row_n) not in right:
                        if col_n > 0 and row_n > 0 and col_n < len(map) and row_n < len(map[0]):
                            right.append((col_n, row_n))

left = True
print(4)
while left == True:
    left = False
    for value in right:
        a = value[0]
        b = value[1]
        if b < (len(map[0])):
            if (a,b+1) not in keys and (a,b+1) not in right:
                right.append((a,b+1))
                left = True
        if b > 0:
            if (a,b-1) not in keys and (a,b-1) not in right:
                right.append((a,b-1))
                left = True
        if a < (len(map)-1):
            if (a+1,b) not in keys and (a+1,b) not in right:
                right.append((a+1,b))
                left = True
        if a > 0:
            if (a-1,b) not in keys and (a-1,b)  not in right:
                right.append((a-1,b))
                left = True
        


second_side = []
for col in range(len(map)):
    for sym in range(len(map[1])):
        if (col, sym) not in right and (col, sym) not in keys:
            second_side.append((col, sym))
            


    
print(len(right))
for a in right:
    if a[0] == 0:
        print("change side")
        break