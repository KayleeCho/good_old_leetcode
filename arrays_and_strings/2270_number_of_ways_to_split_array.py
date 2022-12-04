class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = 0

        print(nums, prefix)

        for i in range(len(nums) - 1):
            left_half = prefix[i]
            right_half = prefix[-1] - prefix[i]
            if left_half >= right_half:
                ans += 1

        return ans