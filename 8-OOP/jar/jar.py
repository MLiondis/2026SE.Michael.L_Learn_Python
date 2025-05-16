class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size
        
    def deposit(self, n):
        if n < 0:
            raise ValueError("cannot add negative cookies")
        elif self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        self.size += n
        return Jar(self.size)

    def withdraw(self, n):
        if n < 0:
            raise ValueError("cannot withdraw negative cookies")
        elif self.size - n < 0:
            raise ValueError("Too many withdrawals fatass")
        self.size -= n
        return Jar(self.size)

    @property
    def capacity(self):
        return self.capacity
    
    @capacity.setter
    def capacity(self, num):
        if num < 0:
            raise ValueError("Capacity must be positive")
        self.capacity = num

    @property
    def size(self):
        return self.size

def main():
    jar = Jar()
    n = int(input("How many cookies do you want to deposit: "))
    jar.deposit(n)
    print(f"{jar.size} cookies in the jar")

if __name__ == "__main__":
    main()