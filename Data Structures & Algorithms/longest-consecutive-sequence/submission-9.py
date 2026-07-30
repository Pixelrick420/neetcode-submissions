class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        vals = set(nums)
        longest = 1
    
        for num in nums:
            if num - 1 not in vals:
                length = 1
                while (num + length) in vals:
                    length += 1

                longest = max(longest, length)
        
        return longest