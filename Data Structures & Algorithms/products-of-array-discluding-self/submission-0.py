class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        prod_l = []
        res = [None] * len(nums)

        for n in nums:
            prod_l.append(curr)
            curr = curr*n

        curr = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] = prod_l[i] * curr
            curr *= nums[i]

        return res

