class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        out = set()

        for i in range(n - 1):
            j, k = i + 1, n - 1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == 0:
                    out.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif curSum > 0:
                    k -= 1
                else:
                    j += 1
            
        return list(out)
                
