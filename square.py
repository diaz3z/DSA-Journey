# Task
# The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4


def sqr(n):
    for i in range(n):
        s = i **2
        print(s)





if __name__ == '__main__':
    n = int(input())
    sqr(n)