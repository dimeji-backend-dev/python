import string
import random

cars = ["volvo","benz","toyota","bugatti","honda","wolkswagen","ferari","BYD"]
number = string.digits + string.ascii_lowercase + string.ascii_uppercase

unique_rand = set()
while len(unique_rand) < len(cars):
    rand = "".join(random.choices(number, k=6))
    unique_rand.add(rand)

unique_id = list(unique_rand)

stock = dict(zip(unique_id, cars))

print(stock)