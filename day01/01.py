# --- Day 1: Trebuchet?! ---
#part1

result = 0

with open ("01.txt", encoding = "utf-8", mode = "r" )  as file:
    for row in file:
        line = row.strip()
        row_numbers = []
        for a in line:
            if a.isdigit():
                row_numbers.append(a)       
        result += (int(row_numbers[0]+row_numbers[-1]))
    print(result)    

# part2
    
result = 0

with open ("01.txt", encoding = "utf-8", mode = "r" )  as file:
    for row in file:
        line = row.strip()
        row_numbers = []
        numbers = {"one": "o1e", "two": "t2o", "three": "thr3w", "four": "fo4r", "five": "fi5e", "six": "s6x", "seven": "se7en", "eight": "eig8t", "nine": "ni9e", "zero": "ze0o"}
       
        for number in numbers.keys():
            if number in line:
                line = line.replace(number, numbers[number])
       
        for a in line:
            if a.isdigit():
                row_numbers.append(a)       
        result += (int(row_numbers[0]+row_numbers[-1]))
    print(result)    
