class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for position in range(n - 2, -1, -1):
            if position + nums[position] >= goal:
                goal = position
        
        return not goal