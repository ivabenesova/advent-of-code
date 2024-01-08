manual = []
numbers_to_count = []

with open ("03.txt", encoding = "utf-8", mode = "r")  as file:
    for row in file:
        longer_row = "." + row.strip() + "."
        manual.append(longer_row)


#numbers and "."
digits_and_dot = ["."]
for num in range(10):
    digits_and_dot.append(str(num))

is_number = False
connected_to = False
number = ""

for row_number in range(len(manual)): 

    row = manual[row_number]

    for symbol_position in range(1,(len(row)-1)):
        
        if row_number == 0:
            positions = (manual[row_number][symbol_position-1],
                             manual[row_number][symbol_position+1],
                             manual[row_number+1][symbol_position-1],
                             manual[row_number+1][symbol_position],
                             manual[row_number+1][symbol_position+1])
        
        elif row_number == (len(manual)-1):
            positions = (manual[row_number][symbol_position-1],
                             manual[row_number][symbol_position+1],
                             manual[row_number-1][symbol_position-1],
                             manual[row_number-1][symbol_position],
                             manual[row_number-1][symbol_position+1])
        
        elif (row_number > 0) and (row_number < (len(manual)-1)):
             positions = (manual[row_number][symbol_position-1],
                             manual[row_number][symbol_position+1],
                             manual[row_number+1][symbol_position-1],
                             manual[row_number+1][symbol_position],
                             manual[row_number+1][symbol_position+1],
                             manual[row_number-1][symbol_position-1],
                             manual[row_number-1][symbol_position],
                             manual[row_number-1][symbol_position+1])
             
        if row[symbol_position].isdigit():
            is_number = True
            number = number + row[symbol_position]

            if connected_to == False:
                for position in positions:
                    if position not in digits_and_dot:
                        connected_to = True

        else:
            if is_number == True and connected_to == True:
                numbers_to_count.append(int(number))
                number = ""
                is_number = False
                connected_to = False
            elif is_number == True and connected_to == False:
                number = ""
                is_number = False

print(sum(numbers_to_count))




                
    