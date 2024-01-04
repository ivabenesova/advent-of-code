card_values = {"A":13, "K":12, "Q":11, "J":0, "T":9, "9":8, "8":7,"7":6, "6":5, "5":4, "4":3, "3":2, "2":1}



cards = dict()

with open("07.txt", mode = "r", encoding = "utf-8") as file:
    
    for row in file:
        card_set = row.strip().split(" ")[0]
        if card_set not in cards:
           cards[card_set] = [int(row.strip().split(" ")[1])]

# 9000 Five of a kind, where all five cards have the same label: AAAAA ok
# 8000 Four of a kind, where four cards have the same label and one card has a different label: AA8AA ok
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
    J_count = 0
    if "J" in occ_dic:
        J_count = occ_dic["J"]
    occ_dic["J"] = 0
    
    values = []
    max_value = 1
    for value in occ_dic.values():
        values.append(value)
        if value > max_value:
            max_value = value
    
    sorted_values = sorted(values, reverse=True)
    print(sorted_values)
    
    J_max_value = sorted_values[0] + J_count
    if len(values) > 1:
        second_value = sorted_values[1]
    
    
    

    if J_max_value == 5:
        classification = 9*10**12
    elif J_max_value == 4:
        classification = 8*10**12
    elif J_max_value == 3:
        if second_value == 2:
            classification = 7*10**12
        else:
            classification = 6*10**12
    elif J_max_value == 2:
        if second_value == 2:
            classification = 5*10**12
        else:
            classification = 4*10**12
    else:
        classification = 3*10**12
    return classification


def clasification_str(str):
    value = 0
    for a in range(len(str)):
        value_a = card_values[str[a]] * (10** ((len(str) - a)*2))
        value += value_a
    return value 

            
for set, bid in cards.items():
    card_seq = occurence(set)
    clas_part1 = (clasification(card_seq))
    print(card_seq, clas_part1)
    cards[set].append(int(clas_part1 + (clasification_str((set)))) )
    print(card_seq)
print(cards)
sorted_cards = {k: v for k, v in sorted(cards.items(), key=lambda item: item[1][1])}

sum = 0
order_num = 0

for seq,bid in sorted_cards.items():
    
    order_num += 1
    bid1 = bid[0]
  
    sum += (bid1*order_num)


print(sum)




    
