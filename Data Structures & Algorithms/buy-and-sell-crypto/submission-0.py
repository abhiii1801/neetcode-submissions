class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        max_p = float("-inf")

        for p in prices:
            curr_min = min(curr_min, p)

            max_p = max(max_p, p - curr_min)

        return max_p




