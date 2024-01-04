

history = []

with open("09.txt", mode = "r", encoding = "utf-8") as file:
    for line in file:
        history.append(line.strip().split(" "))


sum = 0

for line in history:
    zeros = False 

    
    depth = []
    depth.append(line)
    below_line = line
    while zeros == False:
        
        depth_row = []
        for a in range(len(below_line)-1):

            depth_row.append(int(below_line[a+1]) - int(below_line[a]))

        below_line = depth_row
        depth.append(depth_row)
        if depth_row.count(0) == len(depth_row):
            zeros = True
    
    print(depth)

    partial_sum = 0
        
    for a in range(1,len(depth)): #0,1,2
        
        partial_sum = int(depth[-(a)][0]) - partial_sum
    sum = sum + (int(line[0])-partial_sum)
print(sum)
