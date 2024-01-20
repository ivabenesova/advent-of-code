def horizontal_symetric(dataset):
    for index in range(len(dataset)-1):
    
        if dataset[index] == dataset[index+1]:
            num_of_rows = min((len(dataset) - index - 1), (index+1))
           
            upper_side = dataset[(index - num_of_rows+1):index+1]
            lower_side = dataset[(index+1):(index+1+num_of_rows)][::-1] 
            if lower_side == upper_side:
                return index +1
        

def vertical_symetric(dataset):
    transposed_dataset = list(zip(*dataset))    
    vertical_index = horizontal_symetric(transposed_dataset)
    return vertical_index


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
    add_vertical = vertical_symetric(item)         
    add_horizontal = horizontal_symetric(item)
    if isinstance(add_vertical, (int)):
        vertical += add_vertical
    if isinstance(add_horizontal, (int)):
        horizontal += add_horizontal

sum = (horizontal*100) + vertical
print(sum)