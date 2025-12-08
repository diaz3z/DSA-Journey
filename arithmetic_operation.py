# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example


# Print the following:

# 8
# -2
# 15



def operation(a, b):
    sum = a + b
    print(sum)
    diff = a - b
    print(diff)
    product = a * b
    print(product)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    operation(a, b)
