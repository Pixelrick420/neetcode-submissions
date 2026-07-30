class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        n = len(nums)

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            required = -nums[i]
            while(j < k):
                curSum = nums[j] + nums[k]
                if curSum > required:
                    k -= 1
                elif curSum < required:
                    j += 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    while(k > j and nums[k - 1] == nums[k]):
                        k -= 1
                    while(k > j and nums[j + 1] == nums[j]):
                        j += 1
                    k -= 1
                    j += 1
        return out