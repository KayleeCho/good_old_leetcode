class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        summ = sum(nums[:k])
        maximum = summ
        for i in range(1, len(nums) - k + 1):
            summ -= nums[i - 1]
            summ += nums[i + k - 1]
            maximum = max(maximum, summ)
        return float(maximum) / k
