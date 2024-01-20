data = []
with open ("05.txt", encoding = "utf-8", mode = "r" )  as file:
    for row in file:
        data.append(row.strip())


list_of_lists = []
single_list = []

for string in data:
    if not string:
        if single_list:
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


 
        



