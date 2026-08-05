class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for n in s:
            if n - 1 not in s:
                num = n
                cnt = 0
                while num  in s:
                    cnt += 1
                    num += 1
                ans = max(ans, cnt)
            s.add(n)


        return ans
