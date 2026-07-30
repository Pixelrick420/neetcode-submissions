class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for index, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], index]
            
            seen[num] = index
        
        return [-1, -1]