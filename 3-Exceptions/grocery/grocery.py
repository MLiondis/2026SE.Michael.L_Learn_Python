def main():
    grocery_list = []
    while True: 
        try: 
            item = input("Add to your list: ").upper()
        except EOFError: 
            print("\nGrocery List: ")
            break
        else:
            grocery_list.append(item)
    AlphabeticalOrder(grocery_list)

def AlphabeticalOrder(grocery):
    grocery.sort()
    
    make_singular = []
    for item in grocery:
        if item not in make_singular:
            make_singular.append(item)
    for item in make_singular:
        print(f"{grocery.count(item)} {item}")

main()