import csv

with open("Sales Records.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        item_list = []
        total = 0
        for row in reader:
            if row[0] == "Region":
                continue
            item_type = row[2]
            if row[2] == "Fruits":
                total += float(row[13])
        print(total)
        print(item_list)

