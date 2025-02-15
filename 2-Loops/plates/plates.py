def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(s):
	return all([
        start_letters(s),
        characters(s),
        check_last_letter(s),
        no_special_characters(s)
        ])


# makes sure the first 2 digits are letters 
def start_letters(string):
	if string[0:2].isalpha():
		return True

# makes sure the maximum is six and minimum is 2
def characters(string):
	if 2 <= len(string) <= 6:
		return True




def check_last_letter(string):
	#stores the location of the first digit found
	location = None
	# stores the digit that is encountered
	num = ""
	for letter in string:
		#checks for digits in the string
		if letter.isdigit():
			# finds the position of the digit 
			location = string.index(letter)
			# adds the position to num
			num += letter
			break
	
	if string[location:].isdigit():
		if string[location].startswith("0") == False:
			return True



def no_special_characters(string):
	if string.isalnum():
		return True
	else: 
		return False






main()