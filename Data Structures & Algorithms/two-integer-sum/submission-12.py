class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen  = dict()
        n = len(nums)

        for i in range(n):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            
            seen[nums[i]] = i
        
        return [-1, -1]