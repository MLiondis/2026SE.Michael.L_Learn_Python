import csv

with open("UserID.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    for row in data:
        if row