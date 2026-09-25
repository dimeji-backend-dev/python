import string
import random

cars = ["volvo","benz","toyota","bugatti","honda","Volkswagen","ferrari","BYD"]
number = string.digits + string.ascii_lowercase + string.ascii_uppercase

unique_rand = set()
while len(unique_rand) < len(cars):
    rand = "".join(random.choices(number, k=6))
    unique_rand.add(rand)

unique_id = list(unique_rand)

#stock = dict(zip(unique_id, cars))

stock = {}

for i in range(len(cars)):
    stock[unique_id[i]] = cars[i]

#print(stock)

# for car_id, car in stock.items():
#     print(car_id,car)

#print(stock)

data = {'fnm8O4': 'volvo', 'PijEQi': 'benz', '3gtKGm': 'toyota', 'dmIxaf': 'bugatti', 'bHpi9j': 'honda', 'F1SaWl': 'Volkswagen', 'zlEDpp': 'ferrari', 'Np2ZgJ': 'BYD'}

enquiries = input("provide the id of the car you wanted to make the complaint about: ")
if enquiries in data.keys():
    print(data[enquiries])