# This document describes three records:

# The first record lasts 7 milliseconds. The record distance in this record is 9 millimeters.
# The second record lasts 15 milliseconds. The record distance in this record is 40 millimeters.
# The third record lasts 30 milliseconds. The record distance in this record is 200 millimeters.
# Your toy boat has a starting speed of zero millimeters per millisecond. 
# For each whole millisecond you spend at the beginning of the record holding down the button, the boat's speed increases by one millimeter per millisecond.

data = []
record = dict() 


with open("06.txt", mode = "r", encoding = "utf-8") as file:
    for row in file:
        line = row.strip().split(":")
        values = line[1].split(" ")
        cleaned_val = []

        for value in values:
            if value != "":
                cleaned_val.append(value)

        for a in range(0, len(cleaned_val)):
            if (a+1) not in record :
                record[a+1] = {line[0]: cleaned_val[a]} 
            else:
                record[a+1][line[0]] = cleaned_val[a]
total_ways = 1    

for a in range(len(record)):
    time = int(record[a+1]["Time"])
    ways = 0
    for time1 in range(1,time):
        distance = time1*(time-time1)
        if distance > int(record[a+1]["Distance"]):
            ways += 1
    total_ways = total_ways*ways

print(total_ways)
