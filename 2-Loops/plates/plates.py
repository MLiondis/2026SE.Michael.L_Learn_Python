def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(s):
	



# “All vanity plates must start with at least two letters.” (if var was variable then var[0:2] would be va)
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an 
# acceptable vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def start_letters():
	if string[0:2].isalpha():
		return True
	
def characters():
	if len(string) >= 2 and len(string) <= 6:
		return True
	else: 
		return False












main()