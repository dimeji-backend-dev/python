import random
import string

number = [str(num) for num in range(10)]
small_letter = list(string.ascii_lowercase)
capital_letter = list(string.ascii_uppercase)
specials = list(string.punctuation)

combo = number + small_letter + capital_letter + specials

for i in range(5):
    while True:
        otp = "".join(random.choices(combo, k=15))

        number_check = [num.isdigit() for num in otp]
        capital_check = [char.isupper() for char in otp]
        lower_check = [char.islower() for char in otp]
        punct_check = [punct in string.punctuation for punct in otp]

        if (
            number_check.count(True) >= 2
            and capital_check.count(True) >= 2
            and lower_check.count(True) >= 2
            and punct_check.count(True) >= 2
        ):
            print(otp)
            break