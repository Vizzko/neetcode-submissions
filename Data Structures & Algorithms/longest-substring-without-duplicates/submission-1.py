class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        lst = set()
        for right in range(len(s)):
            while s[right] in lst:
                lst.remove(s[left])
                left += 1
            lst.add(s[right])
            best = max(best, len(lst))

        return best