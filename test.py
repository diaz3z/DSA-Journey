
#Pujitha
def search_insert(arr, target):
    low, high = 0, len(arr) - 1
   
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
arr = [1, 3, 5, 6]
target = 5
print("Index:", search_insert(arr, target))  
target = 2
print("Index:", search_insert(arr, target))  
target = 7
print("Index:", search_insert(arr, target))  
target = 0
print("Index:", search_insert(arr, target))  

def singleNumber(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in count:
        if count[num] == 1:
            return num
 
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))


#Mahesh

def single_number(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count == 1:
            return nums[i]

print(single_number([4,1,2,1,2]))

def search_insert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
    return len(nums)

print(search_insert([1,3,5,6], 7))


# Sahithi
