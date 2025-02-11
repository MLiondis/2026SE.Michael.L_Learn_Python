total = 50
coins = [25, 10, 5]
amount_due = total


while amount_due > 0:
    ammount = int(input("Insert Coin: "))

    if ammount in coins:
        amount_due -= ammount
    else:
        print("only 25, 10, or 5 cents are taken here")

    if amount_due > 0:
        print(f"Amount due: {amount_due}")

change = abs(amount_due)
if change >= 0:
    print(f"Here's your change!: {change}")