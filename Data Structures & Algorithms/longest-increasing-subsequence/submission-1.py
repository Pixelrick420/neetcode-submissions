from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def build(index, last):
            if index >= n:
                return 0
            
            elif nums[index] <= last:
                return build(index + 1, last)
            
            else:
                return max(
                    1 + build(index + 1, nums[index]),
                    build(index + 1, last)
                )
        
        return build(0, -1001)