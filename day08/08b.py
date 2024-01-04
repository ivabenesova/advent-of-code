import math


data = []

with open("08.txt", encoding = "utf-8", mode = "r") as file:
    for row in file:
        data.append(row.strip())

instruction = data[0]

network = dict()
for row in data[1:]:
    if row != "":
        network[(row.split("=")[0]).strip()] = [(row.split("=")[1]).strip()[1:4],(row.split("=")[1]).strip()[6:9]]


network_starts = []
network_end = []
for key, value in network.items():
    if key[-1] == "A":
        network_starts.append(key)
print(network_starts)


lengths = []

for each in network_starts:
    print(each)
    code = each
    end = False
    n = 0

    while (end == False):

        for letter in instruction:
            if letter == "L":
                n += 1
                code = network[code][0]

            elif letter == "R":
                code = network[code][1]
                n += 1

        if code[-1] == "Z":
            
            end = True
            lengths.append(n)

print(lengths)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def multiple_lcm(args):
    result = args[0]
    for i in range(1, len(args)):
        result = lcm(result, args[i])
    return result

result = multiple_lcm(lengths)     
print(result)  

      

                 
    

    