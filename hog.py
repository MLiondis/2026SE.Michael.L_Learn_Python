students = [
    {"name": "Hermione", "house": "Gryffindor", "Patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "Patronus": "Stag"}, 
    {"name": "Ron", "house": "Gryffindor", "Patronus": "Jack Russell terrier"}, 
    {"name": "Draco", "house": "Slytherin", "Patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["Patronus"], sep=", ")