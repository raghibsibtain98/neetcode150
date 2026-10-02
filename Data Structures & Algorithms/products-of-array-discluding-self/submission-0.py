class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod,suffix_prod = [],[]
        prefix_product,suffix_product = 1,1


        for i in range(0,len(nums)):
            prefix_prod.append(prefix_product)
            suffix_prod.append(suffix_product)
            prefix_product *= nums[i]
            suffix_product *= nums[len(nums)-i-1]
        
        return [num1*num2 for num1,num2 in zip(prefix_prod,list(reversed(suffix_prod)))]
