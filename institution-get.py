# python program to convert
# json file to csv

import json
import csv

# Open JSON file and loading the data 
# into the variable data

with open('institution-get.json', 'r') as file:
    data = json.load(file)

inst = data["institutions"]
print(inst)
with open('output.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)

    for bank in inst:
    
        name = bank["name"]
        institution = bank["institution_id"]
        oauth = str(bank["oauth"])
        all = name +  "," + institution + "," + oauth + "\n"
        writer.writerow([name,institution,oauth])

        
        # print(name)
        # writer.writerow(name)
    csvfile.close()
