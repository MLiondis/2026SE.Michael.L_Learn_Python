Menu = {
		"Baja Taco": 4.25,
		"Burrito": 7.50,
		"Bowl": 8.50,
		"Nachos": 11.00,
		"Quesadilla": 8.50,
		"Super Burrito": 8.50,
		"Super Quesadilla": 9.50,
		"Taco": 3.00,
		"Tortilla Salad": 8.00
}


def user_input():
	total = 0
	while True:
		try:
			order = input("Order: ").title()
			if order in Menu:
				total += Menu[order]
				print(f"you order costs ${total}")
			else:
				print("Sorry, we don't have serve that here. Would you like to order anything else?")
			continue
		except EOFError:
			print(f"\nyour total is ${total}\nThank you for your order!")
			break


user_input()