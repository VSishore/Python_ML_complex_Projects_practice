import random
import string

def generate_password(min_length, number=True, special_character=True):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation 

    char=letters
    if number:
        char += numbers
    if special_character:
        char += special
    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while ((not meets_criteria) or (len(pwd) < min_length)) :
        new_char = random.choice(char)
        pwd += new_char

        if(new_char in numbers):
            has_numbers = True
        elif(new_char in special):
            has_special = True


        meets_criteria = True
        if(numbers):
            meets_criteria = has_numbers
        if special_character:
            meets_criteria = meets_criteria and has_special

    return pwd


    





min_length=int(input("Enter the length of the password"))
has_number=input("Do you want a number(y/n)").lower() =='y'
has_special=input("do you want special character(y/n)").lower() == 'y'
a = generate_password(min_length , has_number , has_special)
print (a)