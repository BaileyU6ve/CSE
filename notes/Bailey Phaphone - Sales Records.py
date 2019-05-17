import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    item_list = []
    totals_list = []
    totalA = 0
    totalB = 0
    totalC = 0
    totalD = 0
    totalE = 0
    totalF = 0
    totalG = 0
    totalH = 0
    totalI = 0
    totalJ = 0
    totalK = 0
    totalL = 0
    for row in reader:
        item_type = row[2]
        if item_type not in item_list:
            item_list.append(item_type)
        if row[2] == "Fruits":
            totalA += float(row[13])
        if row[2] == "Clothes":
            totalB += float(row[13])
        if row[2] == "Meat":
            totalC += float(row[13])
        if row[2] == "Beverages":
            totalD += float(row[13])
        if row[2] == "Office Supplies":
            totalE += float(row[13])
        if row[2] == "Cosmetics":
            totalF += float(row[13])
        if row[2] == "Snacks":
            totalG += float(row[13])
        if row[2] == "Personal Care":
            totalH += float(row[13])
        if row[2] == "Household":
            totalI += float(row[13])
        if row[2] == "Vegetables":
            totalJ += float(row[13])
        if row[2] == "Baby Food":
            totalK += float(row[13])
        if row[2] == "Cereal":
            totalL += float(row[13])
    totals_list.append(totalA)
    totals_list.append(totalB)
    totals_list.append(totalC)
    totals_list.append(totalD)
    totals_list.append(totalE)
    totals_list.append(totalF)
    totals_list.append(totalG)
    totals_list.append(totalH)
    totals_list.append(totalI)
    totals_list.append(totalJ)
    totals_list.append(totalK)
    totals_list.append(totalL)
    print("Fruits: %s" % totalA)
    print()
    print("Clothes: %s" % totalB)
    print()
    print("Meat: %s" % totalC)
    print()
    print("Beverages: %s" % totalD)
    print()
    print("Office Supplies: %s" % totalE)
    print()
    print("Cosmetics: %s" % totalF)
    print()
    print("Snacks: %s" % totalG)
    print()
    print("Personal Care: %s" % totalH)
    print()
    print("Household: %s" % totalI)
    print()
    print("Vegetables: %s" % totalJ)
    print()
    print("Baby Food: %s" % totalK)
    print()
    print("Cereal: %s" % totalL)
    print("----------------------------")
    print("The highest profit is: %s" % max(totals_list))


def max(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
