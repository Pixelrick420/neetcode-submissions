class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        index = defaultdict(int)
        n = len(nums)

        for i in range(n):
            need = target - nums[i]
            if need in seen:
                return [index[need], i]
            
            seen.add(nums[i])
            index[nums[i]] = i
        
        return [-1, -1]