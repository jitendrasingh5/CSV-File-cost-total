import csv

total = 0
with open("csv/Day54Totals (1).csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Cost"])

        total += float(row["Cost"])

    
    print()
    print(f"Total Cost : {round(total,2)}")