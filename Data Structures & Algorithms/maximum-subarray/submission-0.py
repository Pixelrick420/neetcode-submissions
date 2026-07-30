class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxEnding = nums[0]
        out = maxEnding

        for i in range(1, n):
            maxEnding = max(maxEnding + nums[i], nums[i])
            out = max(out, maxEnding)
        
        return out
