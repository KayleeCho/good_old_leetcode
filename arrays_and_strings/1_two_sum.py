class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):
            complimentary = target - nums[i]
            if complimentary in map:
                return [i, map[complimentary]]
            else:
                map[nums[i]] = i
