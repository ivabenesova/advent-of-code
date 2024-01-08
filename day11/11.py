def get_distance(a,b):
    distance = abs(a[1] - b[1]) + abs(a[0] - b[0])
    return distance

universe_small = []
n = 0
rows_to_expand = []
columns_to_expand = []

with open("11.txt", encoding = "utf-8", mode = "r") as file:
    for row in file:
        universe_row = []
        for symbol in row.strip():
            universe_row.append(symbol)
                
        universe_small.append(universe_row)
        if "#" not in universe_row:
            rows_to_expand.append(n)
        n += 1    

for a in range(len(universe_small[1])):
    list = [x[a] for x in universe_small]
    if "#" not in list:
        columns_to_expand.append(a)

universe_long = []


for a in range(len(universe_small)):
    universe_long.append(universe_small[a])
    if a in rows_to_expand:
        universe_long.append(universe_small[a])

universe_large = []

for row in universe_long:
    long_row = []
    for a in range(len(row)):
        long_row.append(row[a])
        if a in columns_to_expand:     
            long_row.append(row[a])
    universe_large.append(long_row)

galaxy_positions = []
for row in range(len(universe_large)):
    for col in range(len(universe_large[0])):
        if universe_large[row][col] == "#":
            galaxy_positions.append([row, col])

print(galaxy_positions)

dist_sum = 0

for galaxy in galaxy_positions:
    for galaxy2 in galaxy_positions:
        distance = get_distance(galaxy, galaxy2)
        dist_sum += distance

print(dist_sum/2)

