class Solution:    
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.out = set()
        n = len(nums)
        nums.sort()
        
        def generate(index, sublist, curSum):
            if curSum == target:
                self.out.add(tuple(sublist))
                return

            if index >= n or curSum > target:
                return
            
            next = index + 1
            while next < n and nums[next] == nums[index]:
                next += 1
            generate(next, sublist, curSum)

            sublist.append(nums[index])
            generate(index + 1, sublist, curSum + nums[index])
            sublist.pop()
        
        generate(0, [], 0)
        return [list(subset) for subset in list(self.out)]