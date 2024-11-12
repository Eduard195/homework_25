#1
# import json
# with open("data.json", "r") as f:
#     l = json.load(f)
# l1 = []
# for i in l:
#     if i % 3 == 0:
#         l1.append(i)
# print(sum(l1)/len(l1))


#2
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {}
# for v in dict_1.values():
#     dict_2[v] = len(v)
# print(dict_2)

#3
# d1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# d2 = {}

# for k, v in d1.items():
#     d2[k] = []
#     for i in v:
#         if i % 2 != 0:
#             d2[k].append(i)

# print(d2)