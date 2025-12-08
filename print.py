# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# Input Format

# The first line contains an integer .

# Constraints


# Output Format

# Print the list of integers from  through  as a string, without spaces.

# Sample Input 0

# 3
# Sample Output 0

# 123




# def prnt(n):
#     for i in range(1, n + 1):
#         print(i, end="")

# if __name__ == '__main__':
#     n = int(input())
#     prnt(n)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# for i in x, y , z:
#     for j in x, y , z:
#         for k in x, y , z:
#             if i + j + k != n:
#                 print([i, j, k])

newlist = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
