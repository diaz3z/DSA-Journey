# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5



arr = [2, 3, 6, 6, 5]
n = 5

table = {}

for i in arr:
    table[i] = table.get(i, 0) + 1
    print(table)

unique_values = list(table.keys())
print(unique_values)
unique_values.sort(reverse=True)
print(unique_values)
print(unique_values[1])




# new_arr = list(set(arr))
# print(f"New array : {new_arr}")

# arr_sort = sorted(new_arr, reverse=True)
# print(f"printing sorted array {arr_sort}")
# # max_arr = list(max(arr_sort)

# print(arr_sort[1])