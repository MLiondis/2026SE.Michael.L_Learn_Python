def camel_to_snake(user_input):
    snake_case = ""
    for char in user_input:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip("_")

user_text = input("Text: ")

print(camel_to_snake(user_text))

