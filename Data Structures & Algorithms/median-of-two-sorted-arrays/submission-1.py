class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small,large = nums1, nums2

        if len(nums1) > len(nums2) :
            small, large = nums2, nums1
        
        total = len(small) + len(large)
        half = total//2

        l,h = 0, len(small) - 1

        while (True):
            # say small -> 1,2,3,4,5 and large->1,2,3,4,5,6,7,8
            # then l=0,h=3, small_n = 1, this "1" is index, so it means we are taking
            # 2 elements from the "small" array.
            # now large_n = 6 - 1 - 2 = 3, means we are taking 4 elements from "large" array


            small_n = (l+h)//2  #index of elements considered in small
            large_n = (half - small_n - 2) #index of elements considered in large

            smallLeft = small[small_n] if small_n>=0 else float('-inf')
            smallRight = small[small_n+1] if small_n < len(small)-1 else float('inf')
            largeLeft = large[large_n] if large_n>=0 else float('-inf')
            largeRight = large[large_n+1] if large_n < len(large)-1 else float('inf')

            if smallLeft <= largeRight and largeLeft<=smallRight :
                if total%2: 
                    # odd length
                    return min(largeRight,smallRight)
                else:
                    return (max(largeLeft,smallLeft) + min(largeRight,smallRight)) / 2
            elif smallLeft > largeRight:
                h = small_n - 1
            else:
                l = small_n + 1
            
        return 0







        