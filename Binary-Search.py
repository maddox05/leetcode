from typing import List


def search(nums: List[int], target: int) -> int:
    highest = len(nums) - 1
    middle = int(len(nums) / 2)
    lowest = 0
    while True:

        if target == nums[middle]:
            return middle
        elif target == nums[lowest]:
            return lowest
        elif target == nums[highest]:
            return highest
        if highest == middle or lowest == middle:
            return -1
        if target > nums[middle]:
            lowest = middle + 1
            middle = int((lowest + highest) / 2)
        elif target < nums[middle]:
            highest = middle - 1
            middle = int((lowest + highest) / 2)


class Solution:
    pass


hello = Solution()
print(search([1, 2, 3, 4, 5, 6, 12, 15, 16, 18], 12))
