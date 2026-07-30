class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.superSet = []
        n = len(nums)

        def generate(index, subset):
            if index == n:
                self.superSet.append(subset)
                return
            
            generate(index + 1, subset)
            generate(index + 1, subset + [nums[index]])
        
        generate(0, [])
        return self.superSet