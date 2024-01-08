def get_number(string, position):
    num_start = 0
    value = string[position]
    if string[position - 1].isdigit():
        value = str(string[position - 1]) + str(value)
        num_start = - 1
        if string[position - 2].isdigit():
            value = str(string[position - 2]) + str(value)
            num_start = - 2
    if string[position + 1].isdigit():
        value = str(value) + str(string[position + 1])
        if string[position + 2].isdigit():
            value = str(value) + str(string[position + 2])
    value = int(value)
        
    return(value, position + num_start)


manual = []

with open ("03.txt", encoding = "utf-8", mode = "r" )  as file:
    for row in file:
        longer_row = "." + row.strip() + "."
        manual.append(longer_row)

star_number = 0
star_list = dict()

results_list = []


for row_number in range(1, len(manual)-1): 
    row = manual[row_number]
    print(row)
    for symbol_position in range(1,len(manual[row_number])-1):
        
        positions = {0: [-1, -1],
                            1: [-1, 0],
                            2: [-1, 1],
                            3: [0, -1],
                            4: [0, 1],
                            5: [1, -1],
                            6: [1, 0],
                            7: [1, 1],
        }
        
        
        position_list = []
        if row[symbol_position] == "*":
            numbers = set()
               
            for key, direction in positions.items():
                 detected_digit = manual[row_number + direction[0]][symbol_position + direction[1]]
                 
                 if detected_digit.isdigit():
                    digit_row = manual[row_number + direction[0]]
                    number = get_number(digit_row, symbol_position + direction[1])
                    numbers.add(number[0])
            
            results_list.append(numbers)

results = []

for pair in results_list:
    zapis = []
    if len(pair) == 2:
        for a in pair:
            zapis.append(a)
        results.append(zapis)

print(results)

res = 0        
for item in results:
    res +=  item[0]*item[1]

print(res)



                


