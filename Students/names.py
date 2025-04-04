names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for names in sorted(names, reverse=True):
    print(f"hello, {names}")