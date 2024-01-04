card_values = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7,"7":6, "6":5, "5":4, "4":3, "3":2, "2":1}



cards = dict()

with open("07.txt", mode = "r", encoding = "utf-8") as file:
    
    for row in file:
        card_set = row.strip().split(" ")[0]
        if card_set not in cards:
           cards[card_set] = [int(row.strip().split(" ")[1])]

# 9000 Five of a kind, where all five cards have the same label: AAAAA 
# 8000 Four of a kind, where four cards have the same label and one card has a different label: AA8AA 
# 7000 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332 
# 6000 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98 
# 5000 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432 
# 4000 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4 
# 3000 High card, where all cards' labels are distinct: 23456 

def occurence(str):
    occ = dict()
    for symbol in str:
        if symbol not in occ:
            occ[symbol] = 1
        else:
            occ[symbol] += 1
    return occ

def clasification(occ_dic):
    classification = []
    Three = False
    Two = False
    Second_Two = False
    max = 1
    for value in occ_dic.values():

        #Five of kind
        if value == 5:
            classification = 9*10**12
            max = 5
        #four of kind
        elif value == 4:
            classification = 8*10**12
            max = 4
        if value == 3:
            Three = True
            max = 3
        if value == 2:
            if Two == True:
                Second_Two = True
            elif Two != True:
                Two = True
            max = 2
    if max == 1:
        classification = 3*10**12
    elif (Three == True) and (Two == True):
        classification = 7*10**12
    elif Three == True:
        classification = 6*10**12
    elif Two == True:
        if Second_Two == True:
            classification = 5*10**12
        elif Second_Two == False:
            classification = 4*10**12
    return classification        

def clasification_str(str):
    value = 0
    for a in range(len(str)):
        value_a = card_values[str[a]] * (10** ((len(str) - a)*2))
        value += value_a
    return value 

            
for set, bid in cards.items():
    card_seq = occurence(set)
    clas_part1 = clasification(card_seq)
    cards[set].append(int(clas_part1 + (clasification_str((set)))) )

sorted_cards = {k: v for k, v in sorted(cards.items(), key=lambda item: item[1][1])}

sum = 0
order_num = 0
for seq,bid in sorted_cards.items():
    
    order_num += 1
    bid1 = bid[0]
  
    sum += (bid1*order_num)


print(sum)



    
