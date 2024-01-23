with open("14.txt", mode = "r", encoding = "utf-8") as file:
    #transposed_map: north is on the left side
    lines = list(zip(*[x.strip() for x in file.readlines()]))

#order map
ordered = []
for row in lines:
    stone = 0
    gap = 0
    new_line = []
    for index, symbol in enumerate(row):
        if symbol == "O":
            stone += 1    
        elif symbol == ".":
            gap += 1
        elif symbol == "#":
            for _ in range(stone):
                new_line.append("O")
            for _ in range(gap):    
                new_line.append(".")
            new_line.append("#")
            stone = 0
            gap = 0
    for _ in range(stone):
        new_line.append("O")
    for _ in range(gap):    
        new_line.append(".")        
    ordered.append(new_line)        

load = 0

#calculate
for row in ordered:
    for index, symbol in enumerate(row):
        row_value = len(row) - index
        if symbol == "O":
            load += row_value

print(load)
