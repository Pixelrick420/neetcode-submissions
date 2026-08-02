class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.out = set()
        n = len(nums)
        nums.sort()
        
        def generate(index, sublist):
            if index >= n:
                self.out.add(tuple(sublist))
                return
            
            generate(index + 1, sublist)

            sublist.append(nums[index])
            generate(index + 1, sublist)
            sublist.pop()
        
        generate(0, [])
        return list(self.out)