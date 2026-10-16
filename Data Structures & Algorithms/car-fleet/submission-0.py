class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = [(pos,velo) for pos, velo in zip(position,speed)]
        time_stack = []

        for pos, velo in sorted(combined)[::-1] :
            time = (target - pos) / velo
            time_stack.append(time)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2] :
                time_stack.pop()
        
        return len(time_stack)
