vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user = input("Enter text: ")

for vowel in vowels:
    user = user.replace(vowel, "")

print(user)