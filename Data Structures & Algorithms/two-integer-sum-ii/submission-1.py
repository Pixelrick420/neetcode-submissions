class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1

        while(True):
            curSum = nums[left] + nums[right]
            if curSum > target:
                right -= 1
            
            elif curSum < target:
                left += 1
            
            else:
                return [left + 1, right + 1]