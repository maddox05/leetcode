class Solution:

    def twoSum(self, nums, target: int):
        hashy = {}
        for i , n in enumerate(nums):
            if target - n in hashy:
                return [hashy.get(target-n), i]
            hashy[n] = i
