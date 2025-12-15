# Pattern Set 1 – Star Patterns

# Square Star Pattern
# n = 4
# for i in range(1, n+1):
#     print("*" *n)

# def hollowsquare(r, c):
#     for i in range(1, r+1):
#         for j in range(1, c+1):
#             if i ==1 or i == r or j ==1 or j==c:
#                 print("*", end="")
#             else:
#                 print(" ", end="") #
#         print()
# hollowsquare(5, 10)




# Sqaure

# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# * * * * 
# * * * * 
# * * * * 
# * * * * 




# Increasing Triangle

# n = 5
# for i in range(n):
#     for j in range(i +1):
#         print("*", end=" ")
#     print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 



# Inverted Increasing Triangle
# n = 5
# for i  in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

#           * 
#         * * 
#       * * *
#     * * * *
#   * * * * *




# Decreasing Triangle
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

# * * * * * 
# * * * * 
# * * * 
# * *
# *




# Inverted Decreasing Triangle

# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

#   * * * * * 
#     * * * * 
#       * * *
#         * *
#           *





# Pyramid

# num = 5
# for i in range(num):
#     for j in range(i, num):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()



# Inverted Pyramid

# Diamond Pattern

# Number Pyramid

# Alphabet Patterns (A, B, C shapes)