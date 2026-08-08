class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []  # val, index
        res = [0] * len(temp)

        for i, t in enumerate(temp):

            while stack and stack[-1][0] < t:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]

            stack.append([t,i])

        return res



