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


seeds = []
maps = {}
for list in list_of_lists:
    if "seeds" in list[0]:
        seed_list = (list[0].split(":")[1].strip()).split(" ")        

    if "seeds" not in list[0]:
        maps[list[0]] = []
        for a in list[1:]:
            
            number_list = []
            for number in a.split(" "):
                number_list.append(int(number))
            maps[list[0]].append(number_list)

lowest = 9999999999



for n in range(len(seed_list)):
    print(n)

    if n % 2 == 0:
        seed_mapped = int(seed_list[n])
        for condition in maps.values():
            for data in condition:
                
                if (seed_mapped >= data[1]) and (seed_mapped < (data[1] + data[2])):
                    index = seed_mapped - data[1]
                    seed_mapped = data[0] + index
                    break
                else:
                    seed_mapped = seed_mapped
                    continue
                
        if seed_mapped < lowest:
            lowest = seed_mapped    

    if n % 2 != 0:
        maximum = int(seed_list[n])
        for a in range(1, maximum):
            seed_mapped = (int(seed_list[n-1]) + a)
            for condition in maps.values():
                
                for data in condition:
                    if (seed_mapped >= data[1]) and (seed_mapped < (data[1] + data[2])):
                        
                        index = seed_mapped - data[1]
                        seed_mapped = data[0] + index
                        break
                    else:
                        seed_mapped = seed_mapped
                        continue
            if seed_mapped < lowest:
                lowest = seed_mapped        
    
          
print(lowest)
