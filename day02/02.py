# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 
# 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

red_max = 12
green_max = 13
blue_max = 14

possible = []

data = dict()

with open ("02.txt", encoding = "utf-8", mode = "r" )  as file:
    for row in file:
        key = int(row.strip().split(":")[0].split(" ")[1])
        rest = row.strip().split(":")[1].split(";")
        game_stats = dict()
        for sample in rest:
            for color in sample.split(","):
                if "blue" in color:
                    if "blue" in game_stats:
                        game_stats["blue"].append(int(color.strip().split(" ")[0]))
                    else:
                        game_stats["blue"] = [int(color.strip().split(" ")[0])]
                if "red" in color:
                    if "red" in game_stats:
                        game_stats["red"].append(int(color.strip().split(" ")[0]))
                    else:
                        game_stats["red"] = [int(color.strip().split(" ")[0])]
                if "green" in color:
                    if "green" in game_stats:
                        game_stats["green"].append(int(color.strip().split(" ")[0]))
                    else:
                        game_stats["green"] = [int(color.strip().split(" ")[0])]
        data[key] = game_stats

for game, colors in data.items():
    if (max(colors["blue"]) <= blue_max) and (max(colors["red"]) <= red_max) and (max(colors["green"]) <= green_max):
            possible.append(game)

print(sum(possible))

# part2

part2 = []

for game, colors in data.items():
    game_power = max(colors["blue"]) * max(colors["red"]) * max(colors["green"])
    part2.append(game_power)

print(sum(part2))
  

