class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        l = 0

        longest = 0

        for r in range(len(s)):
            if s[r] in se:
                while l < len(s) and s[r] in se:
                    se.remove(s[l])
                    l += 1
            se.add(s[r])

            longest = max(longest, r - l + 1)

        return longest


            

