import csv

with open("Sales Records.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            row = (row[13])


def biggest_num(list):
    tp = list(row[13])
    print("The biggest number is: %s" % max(tp))


print(biggest_num)
