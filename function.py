import random
import string

number = [str(num) for num in range(10)]
small_letter = list(string.ascii_lowercase)
capital_letter = list(string.ascii_uppercase)
specials = list(string.punctuation)

combo = number + small_letter + capital_letter + specials

def checks(otp):
    number_check = [num.isdigit() for num in otp]
    capital_check = [char.isupper() for char in otp]
    lower_check = [char.islower() for char in otp]
    punct_check = [punct in string.punctuation for punct in otp]

    return [number_check,capital_check,lower_check,punct_check]

def requirement(requirements):
    if (
        requirements[0].count(True) >= 2
        and requirements[1].count(True) >= 2
        and requirements[2].count(True) >= 2
        and requirements[3].count(True) >= 2
    ):
        return True
    else:
        return False

def generate_password():
        while True:
            otp = "".join(random.choices(combo, k=16))
            requirements = checks(otp)
            result = requirement(requirements)
            if result == True:
                return otp
while True:
    try:           
        how_many = int(input("how many password do you want? "))
        if how_many <= 0:
            print("Please enter greater than 0: ")
            print()
            continue
        break
    except ValueError:
        print("Please enter a number: ")
        print()

print("\nPassword Generated")
for i in range(how_many):
    password = generate_password()
    print(f"{i + 1}: {password}")
    