# Find negative numbers and replace them with zero
nums = [3, -1, 0, 7, -5, -10, 12]
print(list(map(lambda x: x if x >= 0 else 0, nums)))

# Found users older than 18 and name starts with "O"
users = [
    {"name": "Anna", "age": 22},
    {"name": "Oleg", "age": 17},
    {"name": "Ivan", "age": 30},
    {"name": "Olga", "age": 19}
]
print(list(filter(lambda x: x["age"] > 18 and x["name"].startswith("O"), users)))

# Sort users by age in reverse order
users_1 = [
    {"name": "Anna", "age": 22},
    {"name": "Oleg", "age": 17},
    {"name": "Ivan", "age": 30}
]
users_1.sort(key=lambda x: x["age"], reverse=True)
print(users_1)

#Create list of products where price that is below 10 stay the same it and if bigger than 10 increase price by 50 percents
products = [
    {"name": "apple", "price": 10},
    {"name": "banana", "price": 5},
    {"name": "cherry", "price": 20}
]

print(list(map(lambda x: x if x["price"] < 10 else {**x, "price": x["price"]*1.5}, products)))
