import copy

lst_1 = [[1,2],[3,4]]

lst_2 = copy.deepcopy(lst_1)

lst_1[0][0] = 'x'


print(lst_1)
print(lst_2)