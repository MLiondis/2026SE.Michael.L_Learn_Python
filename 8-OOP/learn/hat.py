import random

class Hat:
    def __init__(self):
        self.houses = ["G", "H", "R", "S"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

name = input("Name: ")

hat = Hat()
hat.sort(name)