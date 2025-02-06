def convert(text: str):
    text = text.replace(":(", "🙁").replace(":)", "🙂")
    return text

def main(): 
    fbn = input("enter text: ")
    print(convert(fbn))

main()