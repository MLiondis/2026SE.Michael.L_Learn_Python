from datetime import date

import inflect

import sys

class Seasons:
    def __init__(self, birth_date, today):
        self.birth_date = birth_date
        self.today = today

    @classmethod
    def get(cls):
        birth = input("Enter birth date (yyyy-mm-dd): ")
        if not birth:
            sys.exit("No date provided")
        try:
            birth_date = date.fromisoformat(birth)
        except ValueError:
            sys.exit("Invalid date format")
        today = date.today()
        return cls(birth_date, today)

    def get_days(self):
        days = (self.today - self.birth_date).days
        return(days * 24 * 60) # converts days to minutes

def convert_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num, andword="")

def main():
    seasons = Seasons.get()
    days = seasons.get_days()
    print(f"{convert_to_words(days)} minutes")

if __name__ == "__main__":
    main()