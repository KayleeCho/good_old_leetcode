class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        last = len(nums)

        targetSum = last * (last + 1) / 2
        return int(targetSum) - sum(nums)
