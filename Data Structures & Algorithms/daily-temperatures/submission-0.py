class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # a problem of monotonic decreasing stack
        # brute force involves standing at an index and 
        # iterating from index+1 to check the 1st occuring greater element

        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures): # 0,1,
            while (len(stack)>0) and (temperatures[stack[-1]] < temp) :
                result[stack[-1]] = index - stack[-1]
                stack.pop()

            stack.append(index)

        return result

        # stack -> 1 
        # result ->1, 0, 0, 0, 0, 0, 0 
                