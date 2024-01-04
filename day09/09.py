import time

history = []

with open("09.txt", mode = "r", encoding = "utf-8") as file:
    for line in file:
        history.append(line.strip().split(" "))


sum = []

for line in history:
    zeros = False 

    
    depth = []
    below_line = line
    while zeros == False:
        
        depth_row = []
        for a in range(len(below_line)-1):
            depth_row.append(int(below_line[a+1]) - int(below_line[a]))

        below_line = depth_row
        depth.append(depth_row)
        if depth_row.count(0) == len(depth_row):
            zeros = True

    partial_sum = 0
    for a in range(len(depth)):
        partial_sum = partial_sum + depth[-(a)][-1] ###???
    sum = sum + (int(line[-1])+partial_sum)


