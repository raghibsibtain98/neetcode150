class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax,rightMax = height[0],height[n-1]
        
        left,right = 0,n-1
        water = 0
        
        while(left<=right): # w = 2
            if (leftMax<=rightMax) :
                water += max(0,leftMax-height[left])
                leftMax = max(leftMax,height[left])
                left +=1
            else:
                water += max(0,rightMax-height[right])
                rightMax = max(rightMax,height[right])
                right -=1
        return water