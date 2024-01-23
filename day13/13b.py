import copy

def horizontal_symetric(dataset):
    horizontal_index = []
    for index in range(len(dataset)-1):
        if dataset[index] == dataset[index+1]:
            num_of_rows = min((len(dataset) - index - 1), (index+1))
           
            upper_side = dataset[(index - num_of_rows+1):index+1]
            lower_side = dataset[(index+1):(index+1+num_of_rows)][::-1] 
            if lower_side == upper_side:
                horizontal_index.append(index+1)
                
    return horizontal_index

def vertical_symetric(dataset):
    transposed_dataset = list(zip(*dataset))    
    vertical_index = horizontal_symetric(transposed_dataset)
    return vertical_index

def replace_symbol(string, index):
    if string[index] == ".":
        new_str = string[:index] + "#" + string[(index+1):]
    elif string[index] == "#":
        new_str = string[:index] + "." + string[(index+1):]
    return new_str


data = []

with open("13.txt", encoding = "utf-8", mode = "r") as file:
    map = []
    for row in file:
        if row.strip():
            map.append(row.strip())
        elif not row.strip():
   
            if map:
                data.append(map)
                map = []
    data.append(map)

horizontal = 0
vertical = 0

for item in data:
    break_cycle = False

    if vertical_symetric(item):
        wrong_vertical = vertical_symetric(item)[0]
    else:
        wrong_vertical = 0   
    if horizontal_symetric(item):       
        wrong_horizontal = horizontal_symetric(item)[0]
    else:
        wrong_horizontal = 0  
    print(item)
    for index_row, map_row in enumerate(item):
        print(map_row)
        for index_el, element in enumerate(map_row):
            
            map_editing = copy.deepcopy(item)   # something new! without copy-decopy was item rewritten with map_editing
            
            map_editing[index_row] = replace_symbol(map_editing[index_row], index_el)

            add_vertical = vertical_symetric(map_editing)      
            add_horizontal = horizontal_symetric(map_editing)

            for value in add_vertical:
                if isinstance(value, (int)) and value != wrong_vertical:
                    vertical += value
                    break_cycle = True
                    
                
            for value in add_horizontal:    
                if isinstance(value, (int)) and value != wrong_horizontal:
                    horizontal += value
                    break_cycle = True
                    
         
            if break_cycle == True:
                break

        if break_cycle == True:
                break
    
    
sum = (horizontal*100) + vertical
print(sum)
