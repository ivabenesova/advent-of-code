import heapq
import copy

with open("17.txt", mode = "r", encoding = "utf-8") as file:
    data = [list(row.strip()) for row in file]

print(len(data), len(data[1]))

min_steps = 1 #change to 4 for part b
max_steps = 3 #change to 10 for part b

position = [0,0]

steps = 0
queue = [(0, 0, 0, 0)] #heat_pos, start_x, start_y, dirc, steps 

visited = []

heapq.heappush(queue, (0, 0, 0, 1))

while queue:    
    heat_pos, start_x, start_y, dirc = heapq.heappop(queue)

    if (start_x == len(data)-1) and (start_y == (int(len(data[0])-1))):
        print("finished", heat_pos)
        break

    if (start_x, start_y, dirc) in visited:
        continue
    
    visited.append((start_x, start_y, dirc))
    
    start = (start_x, start_y)

    new_dirs = []
    new_dirs.append((dirc + 1)%4)
    new_dirs.append((dirc + 3)%4)

    for new_dir in new_dirs:  
        for a in range(min_steps, (max_steps+1)):
            heat = copy.deepcopy(heat_pos)
            
            match new_dir:
                case 0:
                    if (start[1]+a) < len(data[0]):
                        new_pos = (start[0], (start[1]+a))
                        for value in range(1,1+a):
                            heat += int(data[start[0]][start[1]+value])
                        heapq.heappush(queue, (heat, new_pos[0], new_pos[1], new_dir))

                case 1:
                    if (start[0]+a) < len(data):
                        new_pos = ((start[0]+a), start[1])
                        for value in range(1,a+1):
                            heat += int(data[start[0]+value][start[1]])
                        heapq.heappush(queue, (heat, new_pos[0], new_pos[1], new_dir))

                case 2:
                    if (start[1]-a) >= 0:
                        new_pos = (start[0], (start[1]-a))
                        for value in range(1,1+a):
                            heat += int(data[start[0]][start[1]-value])
                        heapq.heappush(queue, (heat, new_pos[0], new_pos[1], new_dir))

                case 3:
                    if (start[0]-a) >= 0:
                        new_pos = ((start[0]-a), start[1])
                        for value in range(1,1+a):
                            heat += int(data[start[0]-value][start[1]])
                        heapq.heappush(queue, (heat, new_pos[0], new_pos[1], new_dir))

   


