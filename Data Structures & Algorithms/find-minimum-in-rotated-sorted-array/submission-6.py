class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]

        n = len(nums)
        left, right = 0, n - 1
        out = 1001

        while(left <= right):
            mid = (left + right) // 2
            if mid == n - 1 or nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            elif nums[mid] > nums[0]:
                out = min(out, nums[mid])
                left = mid + 1
            
            else:
                out = min(out, nums[mid])
                right = mid - 1
        
        return out