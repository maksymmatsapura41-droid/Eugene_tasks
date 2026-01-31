result = list(map(lambda x: 0 if x < 0 else x*2, nums))

result = list(filter(lambda u: u["age"] >= 18 and u["name"].startswith("O"), users))

result = sorted(users, key=lambda u: u["age"], reverse=True)

result = list(map(lambda p: p["price"] if p["price"] <= 10 else p["price"]*1.5, products))

result = list(map(lambda p: p["price"] if p["price"] <= 10 else p["price"]*1.5, products))
