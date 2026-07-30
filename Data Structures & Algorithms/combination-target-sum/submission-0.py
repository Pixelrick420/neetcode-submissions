class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.possible = set()
        n = len(nums)

        def generate(index, subset, curSum):
            if index == n:
                if curSum == target:
                    self.possible.add(tuple(subset))
                return
            

            generate(index + 1, subset, curSum)
            if curSum < target:
                generate(index + 1, subset + [nums[index]], curSum + nums[index])
                generate(index, subset + [nums[index]], curSum + nums[index])
        
        generate(0, [], 0)
        return [list(item) for item in list(self.possible)]