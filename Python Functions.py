# # num = [10, 20, 30]

# # for i, val in enumerate(num):
# #     print(i, val)


# names = ['John', 'Jane', 'Bob', 'Alice']

# for i, name in enumerate(names):
#     print(i, name)

# for i in range(5):
#     print(i)

# for i in range(20):
#     print(i)

# for i in range(0, 20, 2):
#     print(i, end=" ")


a = [1, 2, 4]
b = [10, 30, 20]

for x, y in zip(a, b):
    print(x, y)
    # print(f"Sum{x, y} = {x+y}")