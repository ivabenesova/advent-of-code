data = []
with open ("05.txt", encoding = "utf-8", mode = "r" )  as file:
    for row in file:
        data.append(row.strip())


list_of_lists = []
single_list = []

for string in data:
    if string == "" :
        if single_list != []:
            list_of_lists.append(single_list)
            single_list = []
    else:
        single_list.append(string)
list_of_lists.append(single_list)

print(list_of_lists)

seeds = []
maps = {}
for list in list_of_lists:
    if "seeds" in list[0]:
        seed_list = (list[0].split(":")[1].strip()).split(" ")
        
        for s in seed_list:
            seeds.append(int(s))
            

    if "seeds" not in list[0]:
        maps[list[0]] = []
        for a in list[1:]:
            
            number_list = []
            for number in a.split(" "):
                number_list.append(int(number))
            maps[list[0]].append(number_list)




# describes how to convert a seed number (the source) to a soil number (the destination). 
# This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

# Rather than list every source number and its corresponding destination number one by one, 
# the maps describe entire ranges of numbers that can be converted. Each line within 
# a map contains three numbers: the destination range start, the source range start, and the range length.

# Consider again the example seed-to-soil map:

# 50 98 2
# 52 50 48

# The first line has a destination range start of 50, a source range start of 98, and a range length of 2. 
# This line means that the source range starts at 98 and contains two values: 98 and 99. 
# The destination range is the same length, but it starts at 50, so its two values are 50 and 51. 
# With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.    
            #[79, 14, 55, 13]    
seeds_mapped = []    
for seed in seeds:
    seed_mapped = seed
    for condition in maps.values():
        for data in condition:
            
            if (seed_mapped >= data[1]) and (seed_mapped < (data[1] + data[2])):
                
                index = seed_mapped - data[1]
                seed_mapped = data[0] + index
                break
            else:
                seed_mapped = seed_mapped
                continue
        
    seeds_mapped.append(seed_mapped)
  
print(min(seeds_mapped))


 
        



