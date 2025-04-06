import sys
import csv

def get_name_and_house():
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            first_name = name.split(", ")[1]
            last_name = name.split(", ")[0]
            house = row["house"]
            yield {"first name": first_name, "last name": last_name, "house": house}

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    print("not a valid file")
    sys.exit(1)
elif not sys.argv[1] == "before.csv":
    print("could not read invalid file")
    sys.exit(1)
else:
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
        writer.writeheader()
        for row in get_name_and_house():
            writer.writerow(row)