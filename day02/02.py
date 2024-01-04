# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

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

# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

part2 = []
for game, colors in data.items():
    game_power = max(colors["blue"]) * max(colors["red"]) * max(colors["green"])
    part2.append(game_power)
print(sum(part2))
  

