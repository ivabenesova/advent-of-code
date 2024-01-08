def get_distance_space(a,b, ex_rows, ex_cols):
    row_min = min(a[0], b[0])
    row_max = max(a[0], b[0])
    col_min = min(a[1], b[1])
    col_max = max(a[1], b[1])
    dist_coef = 999999
    plus_n = 0
    for item in ex_rows:
        if row_min < item < row_max:
            plus_n += 1
    for item in ex_cols:
        if col_min < item < col_max:
            plus_n += 1
    
    distance = abs(a[1] - b[1]) + abs(a[0] - b[0]) + plus_n*dist_coef

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

print(columns_to_expand)
print(rows_to_expand)



galaxy_positions = []
for row in range(len(universe_small)):
    for col in range(len(universe_small[0])):
        if universe_small[row][col] == "#":
            galaxy_positions.append([row, col])

dist_sum = 0

for galaxy in galaxy_positions:
    for galaxy2 in galaxy_positions:
        distance = get_distance_space(galaxy, galaxy2, rows_to_expand, columns_to_expand)
        dist_sum += distance

print(dist_sum/2)

