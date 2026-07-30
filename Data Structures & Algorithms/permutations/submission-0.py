class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        n = len(nums)

        def add(permutation, index):
            if index >= n:
                self.permutations.append(permutation)
                return

            for i in range(index + 1):
                add((permutation[:i] + [nums[index]] + permutation[i:]), index + 1)
            
        add([nums[0]], 1)
        return self.permutations