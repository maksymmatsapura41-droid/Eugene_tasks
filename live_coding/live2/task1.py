# Task 1
# Написати функцію remove_all(lst, val), яка видаляє всі входження значення val зі списку lst.
# Умова: зміни мають відбуватися in-place (не можна створювати або повертати новий список,
# потрібно змінити існуючий об'єкт пам'яті).

liiiist = [15,2,3,4,5,6,7,15,9,10,11,12,13,14,15]
def remove_all(lst: list, val) -> list:
    for item in lst:
        if item == val:
            lst.remove(item)
    return lst

print(liiiist)
print(id(liiiist))
remove_all(liiiist, 15)
print(id(liiiist))
print(liiiist)
