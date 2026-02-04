def duplicate(nums):
    hashmap = set()
    for i in nums:
        if i in hashmap:
            return True
        hashmap.add(i)
    return False