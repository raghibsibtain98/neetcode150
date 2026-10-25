class Solution:
    def getMaxValue(self,piles: List[int]):
        max_value = 0
        for pile in piles:
            max_value = max(max_value,pile)
        
        return max_value

    def sumOfHours(self,rate:int,piles:List[int]):
        hours = 0
        for pile in piles:
            hours += (-(pile//-rate))
        
        return hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, self.getMaxValue(piles)
        ans = 0

        while (low<=high) :
            mid = low + (high-low)//2
            actual_hours = self.sumOfHours(mid,piles)
            if (actual_hours<=h):
                high = mid-1
            else:
                low = mid+1
        
        return low