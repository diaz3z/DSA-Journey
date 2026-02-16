nums = [26, 45, 78, 92, 49, 25]
nums.sort()
print(f"Sorted array {nums}")
target = 45


def binarySeach(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            print(f"Targe value is at index {mid}")
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        
    return -1



binarySeach(nums=nums, target=target)