# Task5

# Умова:
# Дано список рядків (слів). Написати функцію, яка згрупує слова, що є анаграмами одне одного.
# Анаграми - це слова, які складаються з однакових літер у різній послідовності.
#
# Приклад:
#
# Вхід: ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Вихід: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
from collections import defaultdict

l = ["eat", "tea", "tan", "ate", "nat", "bat"]

def func(l: list):
    dic = defaultdict(list)
    for n in l:
        key = "".join(sorted(n))
        dic[key].append(n)
    return list(dic.values())

print(func(l))