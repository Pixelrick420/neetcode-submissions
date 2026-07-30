class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = set(nums)
        out = 1

        for num in nums:
            if (num - 1) not in unique:
                cur = 1
                while (num + 1) in unique:
                    cur += 1
                    num += 1
                
                out = max(out, cur)
        
        return out