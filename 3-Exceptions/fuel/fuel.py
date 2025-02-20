def main():
    while True:
        try:
            x, y = input("Enter fuel: ").split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError("The denominator cannot be zero")


            fuel_percentage = (x / y) * 100

            if fuel_percentage < 1.0:
                print("E")
            elif fuel_percentage > 99.0:
                print("F")
            else:
                print(f"Fuel level is {fuel_percentage:.1f}%")
                break
            
        except ValueError:
            print("invalid input, please enter a valid fuel level")

main()