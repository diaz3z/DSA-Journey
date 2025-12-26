# expense = [2200, 2350, 2600, 2130, 2190]
# extra = expense[1] - expense[0]
# print(f"Extra expense in Fabruary: {extra}")
# print()

# total_quater = expense[0] + expense[1] + expense[2]
# print(f"Total expense in first quater: {total_quater}")
# print()

# for i in expense:
#     if i == 2000:
#         print(f"Spend 2000 in {i}")
#     else:
#         print(f"Doesn't spend exactly 2000 in any month")

# print()

# june_expense = 1980
# expense.append(june_expense)
# print(f"updated Expense list after june: {expense}")
# print()

# refund = 200
# expense[3] = expense[3] + refund
# print(f"updated list after refund { expense}")



# heros=['spider man','thor','hulk','iron man','captain america']

# print(f"Printing the lenght of the list: {len(heros)}")
# print()

# heros.append("black panther")
# print(f"Updated list after adding black panther {heros}")
# print()


# heros.pop()
# heros.insert(3, "black panther")
# print(f"Updated list after adding black panther after hulk: {heros}")
# print()


# heros[1:3] = ["Doctor Strange"]
# print(f"Updated list after adding doctor strange {heros}")
# print()

# # print(dir(list))
# heros.sort()
# print(f"Printing sorted list alphabetical order {heros}")



# max_user = int(input("Add some no."))
# list1 = []
# for i in range(1, max_user):
#     if i % 2 != 0:
#         list1.append(i)
#     else:
#         pass
# print(f"List of all odd numbers {list1}")



# arr = [6, 1, 6, 5, 8, 4]
#         # max_el = max(arr)
# sort_arr = sorted(arr)
# print(sort_arr, "sorted array")
# print(sort_arr[-1] + sort_arr[-2] + sort_arr[-3])


# Love Babbar DSA Questions


# arr = [1, 4, 3, 2, 6, 5]  
# arr = arr[::-1]
# print(arr)

# arr = [22, 14, 8, 17, 35, 3]
# N = len(arr)

# mini = arr[0]
# maxi = arr[0]

# for i in range(N):
#     if arr[i] > maxi:
#         maxi = arr[i]
#     elif arr[i] < mini:
#         mini = arr[i]
# print(f" {maxi}, {mini}")

# arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
# k = 4
# arr.sort()
# print(arr)
# print(arr[k-1])


# arr = [0, 1, 2, 0, 1, 2, 5, 9, 5]

# low = 0
# mid = 0
# high = len(arr) - 1

# while mid <= high:
#     if arr[low] == 0:
#         arr[low], arr[mid] = arr[mid], arr[low]
#         mid += 1
#         low += 1
#     elif arr[mid] == 1:
#         mid += 1
#     elif arr[mid] == 2:
#         arr[mid], arr[high] = arr[high], arr[mid]
#         high -= 1


# print(arr)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict['brand'])
# print(thisdict.get('model'))
# print(list(thisdict.keys()))
# print(thisdict.keys())
# print(tuple(thisdict.keys()))
# thisdict['color'] = 'black'

# print(list(thisdict.keys()))
# print(thisdict.get('model'))
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())

# if "model" in thisdict:
#     print("Model key is available in dictionary!")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["year"] = 1954
# thisdict.update({'year': 2020})
# thisdict.pop('brand')
# thisdict.popitem()
# del thisdict["brand"]
# thisdict.clear()

# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(len(thisdict))




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # for x in thisdict.values():
# # for x in thisdict.keys():
# for x in thisdict.items():
#     print(x)



# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y + ":", obj[y])



arr = [1, 4, 3, 2, 6, 5]
arr = arr[::-1]
print(arr)