import random
import string

def generate_password(length_of_password=0,include_numbers=False,include_special_characters=False):
    alphabets_upper_lowercase = [ letter for letter in string.ascii_letters]    
    numbers = [number for number in string.digits ]
    special_characters = [ char for char in string.punctuation ]

    if include_special_characters == True and include_numbers == True:
        all_characters = alphabets_upper_lowercase + numbers + special_characters
        generated_password = random.sample(all_characters,k=length_of_password)
    elif include_special_characters == False and include_numbers == True:
        all_characters = alphabets_upper_lowercase + numbers
        generated_password = random.sample(all_characters,k=length_of_password)
    elif include_special_characters == True and include_numbers == False:
        all_characters = alphabets_upper_lowercase + special_characters
        generated_password = random.sample(all_characters,k=length_of_password)
    else:
        all_characters = alphabets_upper_lowercase
        generated_password = random.sample(all_characters,k=length_of_password)

    return "".join(generated_password)       

#First asks the user what they want in thier password 
length_of_password = input("Enter length of password: ")

if length_of_password.isdigit() == False:
    print("Invalid length please enter a number greater than 0 :( ")
    quit()
else:
    length_of_password = int(length_of_password)

include_numbers = input("Do you want to numbers in your password ?(y/n) ")
if "y" in include_numbers or "Y" in include_numbers:
    include_numbers = True
else:
    include_numbers = False

special_characters = input("Do you want special characters in your password ?(y/n) ")
if "y" in special_characters or "Y" in special_characters:
    special_characters = True
else:
    special_characters = False

print()
print(generate_password(length_of_password,include_numbers,special_characters))

