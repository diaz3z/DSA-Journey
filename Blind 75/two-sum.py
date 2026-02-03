"""
nums = 
target = 

return indices of nums which add up to target.
e.g. 
nums = [2,5,9,6]
target = 11
2+9 = 11 
indices of "2" and "9"

"""

class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return prevMap[diff], i
            prevMap[val] = i
        return