class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefProduct = [1] * (n + 1)
        suffProduct = [1] * (n + 1)

        out = []

        for i in range(1, n + 1):
            prefProduct[i] = (prefProduct[i - 1] * nums[i - 1])

        for i in range(n, 0, -1):
            suffProduct[i - 1] = (suffProduct[i] * nums[i - 1])
        
        for i in range(n):
            out.append(prefProduct[i] * suffProduct[i + 1])
            
        return out
