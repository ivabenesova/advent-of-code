data = []

with open("08.txt", encoding = "utf-8", mode = "r") as file:
    for row in file:
        data.append(row.strip())

instruction = data[0]

network = dict()
for row in data[1:]:
    
    if row != "":
        network[(row.split("=")[0]).strip()] = [(row.split("=")[1]).strip()[1:4],(row.split("=")[1]).strip()[6:9]]


n = 0
#code0
code = "AAA"
end = False

while end == False:
    
    
    for letter in instruction:
        if letter == "L":
            n += 1
            code = network[code][0]
            
        elif letter == "R":
            code = network[code][1]
            n += 1
            
    if code == "ZZZ":
        
        end = True

print(n)
            
    

    