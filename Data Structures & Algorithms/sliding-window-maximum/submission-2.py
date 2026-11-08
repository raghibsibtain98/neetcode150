class Solution:
    #[1,2,1,0,4,2,6] k-> 3
    # dq -> 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r,l=0,0
        dq = collections.deque()
        result = []

        while (r<len(nums)):
            while dq and nums[dq[-1]] < nums[r] :
                dq.pop()

            dq.append(r)
            if dq[0]<l:
                dq.popleft()
            
            if r >= k-1:
                l+=1
                result.append(nums[dq[0]])

            r+=1

        return result