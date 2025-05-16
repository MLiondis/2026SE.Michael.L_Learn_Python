class Jar:
    total = 0

    def __init__(self, capacity=12):
        self.dih = capacity

    def __str__(self):
        return "🍪" * self.size
        
    def deposit(self, n):
        if n < 0:
            raise ValueError("cannot add negative cookies")
        elif self.size + n > self.dih:
            raise ValueError("Too many cookies")
        self.total += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("cannot withdraw negative cookies")
        elif self.total - n < 0:
            raise ValueError("Too many withdrawals fatass")
        self.total -= n

    @property
    def capacity(self):
        return self.dih

    @property
    def size(self):
        return self.total

def main():
    jar = Jar(capacity=100)
    n = int(input("How many cookies do you want to deposit: "))
    jar.deposit(n)
    print(f"{jar.size} cookies in the jar")
    print(jar.__str__())


if __name__ == "__main__":
    main()