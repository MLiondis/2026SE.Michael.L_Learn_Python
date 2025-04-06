from tabulate import tabulate 
import sys
import csv

new_table = []

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)
else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_table.append(row)
            print(tabulate(new_table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)