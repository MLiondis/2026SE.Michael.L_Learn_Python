#def main():
    #fuel = input("Enter fuel: ")
    #print("Fuel level is", (x / y),"%")
    #if convert(fuel) < 0.01:
        #print("E")
    #elif convert(fuel) > 0.99:
        #print("F")


x, y = input("Enter fuel: ").split("/")
x = int(x)
y = int(y)
fuel = (x / y * 100, "%")
print(fuel)

if fuel < 1.0:
    print("E")
elif fuel > 99.0:
    print("F")


#main()