data = []
record = dict() 


with open("06.txt", mode = "r", encoding = "utf-8") as file:
    for row in file:
        line = row.strip().split(":")
        values = line[1]
        cleaned_val = ""

        for symbol in values:
            if symbol.isdigit():
                cleaned_val += symbol
        
        record[line[0]] = int(cleaned_val)


total_ways = 0   

time = int(record["Time"])

for time1 in range(1,time):
    distance = time1*(time-time1)
    if distance > int(record["Distance"]):
        total_ways += 1

print(total_ways)