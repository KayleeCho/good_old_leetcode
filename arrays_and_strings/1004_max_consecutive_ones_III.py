class Solution(object):
    def longestOnes(self, nums, k) -> int:

        #     [1,1,1,0,0,0,1,1,1,1,0]
        #            i
        #                j

        #                c =2

        i, j = 0, 0
        max_len = 0
        counter = 0
        while j < len(nums):
            if nums[j] == 0:
                counter += 1
            while counter > k:
                # shrink window
                if nums[i] == 0:
                    counter -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
