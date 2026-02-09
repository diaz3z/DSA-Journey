
def maxProduct(nums):
    res = max(nums)

    curMin, curMax = 1, 1

    for i in nums:
        if i == 0:
            curMin, curMax = 1, 1
            continue

        tmp = curMax * i
        curMax = max(i * curMax, i * curMin, i)
        curMin = max(tmp, i * curMin, i)
        res = max(res, curMax)
    return res