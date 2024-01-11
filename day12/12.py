

def generate_combinations(string):

    index = string.find('?')
    if index != -1:
        return (
            generate_combinations(string[:index] + '.' + string[index + 1:]) +
            generate_combinations(string[:index] + '#' + string[index + 1:])
        )
        
    else:
        return [string]


def is_fit(combination, pattern):
    
    pattern_to_compare = []

    start = True
    length = 0

    for num in range(len(combination)):

        if combination[num] == "#":
            start = False
            length += 1
     
        elif combination[num] == "." and (start == False):
            start = True
            pattern_to_compare.append(length)
            length = 0
           
        elif combination[num] == "." and (start == True):  
            start = True
            
    
    if combination[-1] == "#":
        pattern_to_compare.append(length)

    elif combination[-1] == "." and (start == False):
        pattern_to_compare.append(length)

        
    if pattern == pattern_to_compare:
        return True
    
    else:
        return False
    

data = []

test_list = []
with open("12.txt", encoding = "utf-8", mode = "r") as file:

    for row in file:
        a, b = row.strip().split(" ")
        numbers = []
        for num in b.split(","):
            numbers.append(int(num))
        data.append([a,numbers])


sum = 0
list_of_arrangements = []

for list in data:
    
    combination_list = generate_combinations(list[0])

    arrangments = 0

    for item in combination_list:

        if is_fit(item, list[1]):
           
            arrangments += 1
        
    list_of_arrangements.append(arrangments)
    sum += arrangments

print(sum)














