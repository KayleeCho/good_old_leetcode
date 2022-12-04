class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # time complexity: O(n)

        # space complexity : O(k) k is the number of unique characters in your string
        longest = 0
        l = 0
        lib = {}

        for r, c in enumerate(s):
            if c in lib:
                l = max(l, lib[c] + 1)

            lib[c] = r
            longest = max(r - l + 1, longest)

        return longest