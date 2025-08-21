from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []





# nums = [3,4,5,6]
# target = 7
# nums = [4,5,6]
# target = 10

nums = [5,5]
target = 10

print(twoSum(nums, target))




