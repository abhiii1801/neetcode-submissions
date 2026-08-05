class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            if heights[l] <= heights[r]:
                area = width * heights[l]
                l += 1
            else:
                area = width * heights[r]
                r -= 1

            res = max(res, area)

        return res


