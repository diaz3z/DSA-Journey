# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example


# The result of the integer division .
# The result of the float division is .
# Print:

# 0
# 0.6



def status(a, b):
    division = a / b
    print(int(division))
    print(division)
    


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    status(a, b)

