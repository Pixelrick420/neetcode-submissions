class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * (n + 1)
        post = [1] * (n + 1)
        
        for i in range(1, n + 1):
            pref[i] = nums[i - 1] * pref[i - 1]
            post[n - i] = nums[n - i] * post[n - i + 1]
        
        output = []
        for i in range(n):
            output.append(pref[i] * post[i + 1])
        return output