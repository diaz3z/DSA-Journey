# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0

# n =3
# n is odd and odd numbers are weird, so print Weird.



def status(n):
    if n % 2 != 0:
        return "Weird"
    elif n in range(2, 6):
        return "Not Weird"
    elif n in range(6, 12):
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    result = status(n)
    print(result)