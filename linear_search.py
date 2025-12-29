def linear(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


arr = [4, 2, 3, 1, 5, 7, 9, 6, 8]
target = 7
result = linear(arr, target)
print(result)