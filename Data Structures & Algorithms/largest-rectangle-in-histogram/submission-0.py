class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            curr_index = index
            while(stack and stack[-1][1] > height) :
                max_area = max(max_area, (stack[-1][1] * (index-stack[-1][0])))
                curr_index = stack[-1][0]
                stack.pop()
            stack.append((curr_index,height))

        while (stack) :
            max_area = max(max_area, (stack[-1][1] * (n-stack[-1][0])))
            stack.pop()
        
        return max_area

        