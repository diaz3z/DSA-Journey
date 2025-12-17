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


# num = 5

# for i in range(num):
#     for j in range(i + 1):
#         if i % 2 == 0:
#             print("A", end=" ")
#         else:
#             print("B", end=" ")
#     print()


# num = 5
# for i in range(num):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, num):
#         print("*", end=" ")
#     print()


# num = 5
# p = 1
# for i in range(num):
#     for j in range(i + 1):
#         print(p, end=" ")
#         p += 1
#     print()



# num = 5
# for i in range(num):
#     for j in range(i + 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()



# num = 5
# for i in range(num-1):
#     for j in range(i + 1):
#         print("*", end=" ")
#     for j in range(i, num-1):
#         print(" ", end=" ")
#     for j in range(i, num-1):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(num):
#     for j in range(i, num):
#         print("*", end=" ")
#     for j in range(i ):
#         print(" ", end=" ")
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i, num):
#         print("*", end=" ")
#     print()




# num = 5
# for i in range(num-1):
#     for j in range(i, num):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, num-1):
#         print("*", end=" ")
#     for j in range(i, num):
#         print("*", end=" ")
#     print()





# num = 5
# for i in range(num-1):
#     for j in range(i, num):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(num):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, num-1):
#         print("*", end=" ")
#     for j in range(i, num):
#         print("*", end=" ")
#     print()


# num = 5

# z = 1
# print(" *" * num, end=" ")
# print()
# for i in range(1, num):
#     print(" " * z, "* " * 1, " " * (num-2), " *" * 1)
#     z +=1
#     if z == (num -1):
#         print(" " * z, "* " * num, end=" ")
#         break




# row = 5
# col = 10
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if i == 1 or i == row or j == 1 or j == col:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()