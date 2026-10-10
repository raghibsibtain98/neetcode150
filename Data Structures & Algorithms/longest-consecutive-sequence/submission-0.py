class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collect = set(nums)
        longest = 0
        length = 0
        for num in nums:
            if num-1 not in collect:
                length = 0         #num is starting point
                while (num + length) in collect:
                    length += 1
                longest = max(length,longest)

        return longest