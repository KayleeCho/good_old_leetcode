class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        j = len(s) - 1
        for i in range(len(s)):
            if i < j:
                front = s[i]
                end = s[j]
                s[j] = front
                s[i] = end
                j -= 1
