# functions = []
#
# for n in range(1, 6):
#     functions.append(lambda m = n: m * m)
#
# for func in functions:
#     print(func())
from struct import unpack


# def add_to_inventory(item, inventory=[]):
# 	inventory.append(item)
# 	return inventory
#
# print(add_to_inventory("Sword"))
# print(add_to_inventory("Shield"))
# print(add_to_inventory("Potion"))

# ls = [1,2,3,4,5,6,7]
# low, *mid, max, maxmax = ls
# print(low)
# print(mid)
# print(max)
# print(maxmax)

# players = ["gonD", "Pir", ""]
# def can_start_raid(players):
# 	return all(players) and bool(players)
#
# print(can_start_raid(players))

# base_stats = {"hp": 100, "mp": 50, "speed": 10}
# buffs = {"speed": 15, "luck": 5}
#
# print(base_stats | buffs)


# scout_a = ["Orc", "Goblin", "Troll", "Dragon"]
# scout_b = ["Dragon", "Troll", "Skeleton"]
#
# print(set(scout_a) & set(scout_b))


# items = ["Sword", "Shield", "Potion"]
# prices = [500, 300, 50]
# print(dict(zip(items, prices)))

# enemies = [
#     {"name": "Orc", "hp": 50},
#     {"name": "Dragon", "hp": 500},
#     {"name": "Goblin", "hp": 20}
# ]
#
#
# enemies.sort(key = lambda x: x["hp"])
# print(enemies)