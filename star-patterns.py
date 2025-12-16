# num = 5
# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, num-1):
#         print("*", end=" ")
#     for j in range(i, num):
#         print("*", end=" ")
#     print()


# num = 5
# for i in range(num):
#     for j in range(i +1):
#         print("*", end=" ")
#     print()


num = 5

for i in range(num):
    for j in range(i + 1):
        if i % 2 == 0:
            print("A", end=" ")
        else:
            print("B", end=" ")
    print()






