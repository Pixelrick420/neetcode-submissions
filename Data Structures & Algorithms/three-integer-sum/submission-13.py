class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()

        for i in range(0, n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                cur =  nums[i] + nums[j] + nums[k]
                
                if cur > 0:
                    k -= 1
                
                elif cur < 0:
                    j += 1
                
                else:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
        out = []
        for triplet in triplets:
            out.append(list(triplet))

        return out
