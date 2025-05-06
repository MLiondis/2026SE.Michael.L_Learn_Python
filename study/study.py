import csv

with open("UserID.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["username", "password"])
    writer.writeheader()

start = input("Login, Register, or Exit? ")

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open("UserID.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writerow({"username": username, "password": password})
        print("User registered successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("UserID.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row["username"] and password == row["password"]:
                print("Login Successful!")
                logout = input("Logout or Change password? ")
                if logout == "Logout":
                    print("logged out successfully")
                    break
                elif logout == "Change password":
                    new_password = input("Enter new password: ")
                    with open("UserID.csv", "r") as file:
                        reader = csv.DictReader(file)
                        data = list(reader)
                        for row in data:
                            if row["username"] == username:
                                row["password"] = new_password
                    with open("UserID.csv", "w") as file:
                        writer = csv.DictWriter(file, fieldnames=["username", "password"])
                        writer.writeheader()
                        writer.writerows(data)
                    print("Password changed successfully!")
                    break
            else:
                print("Incorrect username or password.")
                break

if start == "Exit":
    print("Goodbye!")
    exit()
elif start == "Register":
    register()
    start1 = input("Login or Exit? ")
    if start1 == "Exit":
        print("Goodbye!")
        exit()
    elif start1 == "Login":
        login()
elif start == "Login":
    login()