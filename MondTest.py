#create 2 lists of items
#print as table
#user input an item to ap promt and only that name from the table prints
#add a new item and sort
#create text dc with the lsits
#read from the lists
#edit lines and write to lists

list1 = ["John", "Marvin", "Tim"]
list2 = ["Pork", "Beak", "cheese"]

def main():
    add_item()
    user_item()

def print_lists():
    if len(list1) >= len(list2):
        i = 0
        for things in list1:
            print(f"| {list1[i]} | {list2[i]} |")
            i += 1
    elif len(list1) <= len(list2):
        i = 0
        for things in list2:
            print(f"| {list1[i]} | {list2[i]} |")
            i += 1

def add_item():
    while True:
        try:
            item_1 = input("New Item: ")
            item_2 = input("New Item equals: ")
            list1.append(item_1)
            list2.append(item_2)
            # list1.sort()
            # list2.sort()
            print_lists()
        except EOFError:
            print()
            break

def user_item():
    while True:
        try:
            item = input("find item: ")
            for i in range(len(list1)):
                if item == list1[i]:
                    print(list2[i])
            for i in range(len(list2)):
                if item == list2[i]:
                    print(list1[i])
        except EOFError:
            print()
            break

if __name__ == "__main__":
    main()

# learn hashing - incryts a piece of data to turn it into 10 characters
# learn b literal like byte conversion - converts to a byte 