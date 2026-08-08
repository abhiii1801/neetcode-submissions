class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #start_idx, height
        max_area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popped = stack.pop()
                start = popped[0]
                width =  i - start
                max_area = max(max_area, width * popped[1])
            
            stack.append([start, h])

        while stack:
            popped = stack.pop()
            width = len(heights) - popped[0]
            max_area = max(max_area, width * popped[1])

        return max_area


