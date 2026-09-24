import string
import random

cars = ["volvo","benz","toyota","bugatti","honda"]
number = string.digits + string.ascii_lowercase + string.ascii_uppercase

unique_rand = set()
while len(unique_rand) < 5:
    rand = "".join(random.choices(number, k=6))
    unique_rand.add(rand)

unique_id = list(i for i in unique_rand)

stock = {
            unique_id[0]:cars[0],
            unique_id[1]:cars[1],
            unique_id[2]:cars[2],
            unique_id[3]:cars[3],
            unique_id[4]:cars[4]
        }

print(stock)