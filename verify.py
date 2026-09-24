import string
import random
cars = ["volvo","benz","toyota"]
number = string.digits + string.ascii_lowercase + string.ascii_uppercase
print(cars)
print(number)

unique_rand = set()

while len(unique_rand) < 5:
    rand = "".join(random.choices(number, k=6))
    unique_rand.add(rand)

for rand in unique_rand:
        print(rand)