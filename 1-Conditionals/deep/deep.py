ans = input("What is the meaning of life? ")

match ans:
    case "42" | "Forty-two" | "Forty two" | "forty-two" | "forty two":
        print("Yes!")
    case _:
        print("No")


