class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            curr = nums[i]

            if i >0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            remain = 0  - curr

            while l < r:
                summ = nums[l] + nums[r]
                if summ == remain:
                    res.append([nums[l], nums[r], curr])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1


                elif summ < remain:
                    l += 1
                else:
                    r -= 1

        return res







