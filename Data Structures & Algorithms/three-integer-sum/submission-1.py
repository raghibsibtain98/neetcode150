class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        for index, num in enumerate(nums):
            if index>0 and num==nums[index-1]:
                continue
            else:
                left, right = index+1, n-1
                while (left < right) :
                    if nums[left] + nums[right] + num > 0 :
                        right -=1
                    elif nums[left] + nums[right] + num < 0 :
                        left += 1
                    else :
                        result.append([nums[index],nums[left],nums[right]])
                        left+=1
                        while (nums[left]==nums[left-1] and left<right):
                            left+=1
        
        return result


        # -4, -1, -1, 0, 1, 2