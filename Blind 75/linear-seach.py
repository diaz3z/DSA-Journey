nums = [26, 45, 78, 92, 49, 25]
target = 49

def linearSeach(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            print(f"Element found at {i}")
            return i
        
    return -1



linearSeach(nums=nums, target=target)