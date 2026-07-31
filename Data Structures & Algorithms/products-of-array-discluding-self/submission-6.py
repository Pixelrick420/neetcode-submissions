class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * (n + 1)
        post = [1] * (n + 1)

        for i in range(1, n + 1):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        for i in range(n - 1, -1, -1):
            post[i] = nums[i]  * post[i + 1]
        
        out = []
        print(pref, post)
        for i in range(n):
            out.append(pref[i] * post[i + 1])
        
        return out