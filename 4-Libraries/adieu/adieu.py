import inflect
p = inflect.engine()

name = []

while True:
    try: 
        names = input("Names: ")
        name.append(names)
    except EOFError:
        test = p.join((name))
        print("\nAdieu, Adieu, to", test)
        break