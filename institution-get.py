# python program to convert
# json file to csv

import json
import csv

# Open JSON file and loading the data 
# into the variable data

with open('institution-get.json', 'r') as file:
    data = json.load(file)

inst = data["institutions"]
cleaned = [] 
print(inst)
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
csv_writer=csv.writer(inst)

# counter variable used for writing 
# headers to the csv file

count = 0

for bank in inst:
    if count == 0:

        # writing headers of csv file
        header = inst.keys()
        # writing data of csv file
        csv_writer.writerow(header)
        count += 1
    print(bank["name"])
    print(bank["institution_id"])
    print(bank["oauth"])
    print("") 
    name = bank["name"]
    institution = bank["institution_id"]
    oauth = bank["oauth"]
    writer.writerows("data")

    
    # print(name)
    # writer.writerow(name)

