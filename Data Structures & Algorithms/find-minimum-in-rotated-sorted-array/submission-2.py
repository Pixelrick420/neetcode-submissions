class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        out = float('inf')

        while left <= right:
            if nums[left] < nums[right]:
                out = min(nums[left], out)
                break

            mid = (left + right) // 2
            out = min(out, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1

            else:
                right = mid - 1
        
        return out
            

