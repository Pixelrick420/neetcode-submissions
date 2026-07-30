class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in uniq:
                count = 1
                while (num + count) in uniq:
                    count += 1
                longest = max(longest, count)
            
        return longest