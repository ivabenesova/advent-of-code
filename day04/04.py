cards = dict()
cards2 = dict()
card_list = []

with open ("04.txt", encoding = "utf-8", mode = "r" )  as file:
    
    for row in file:
        card_list.append(row)
                
for row in card_list:  
    card_name =  (row.strip().split(":")[0])
    card_num = ""
    for symbol in card_name:
        if symbol.isdigit():
            card_num += symbol
    card_num = int(card_num)
    cards[card_num] = 1
    cards2[card_num] = 1  
  
for row in card_list: 
    card_name =  (row.strip().split(":")[0])
    card_num = ""
    for symbol in card_name:
        if symbol.isdigit():
            card_num += symbol
    card_num = int(card_num)
     
    winning_numbers = ((row.strip().split(":")[1]).split("|")[0]).strip().split(" ")
    my_numbers = ((row.strip().split(":")[1]).split("|")[1]).strip().split(" ")
    n = 0
    for my_number in my_numbers:
        if my_number != "":
            if my_number in winning_numbers:
                n += 1
    for a in range(1,n+1):
        total_cards = cards[card_num]
        index = card_num + a
        cards[index] += (1*total_cards)
    print(card_num, n, total_cards)   


suma = 0
for number in cards.values():
      suma += number    

print(suma)