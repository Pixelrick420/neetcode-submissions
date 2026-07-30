class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * (n + 1)
        sufix_prod = [1] * (n + 1)
        out = []

        pref = 1
        suf = 1
        for i in range(n):
            prefix_prod[i] = pref
            sufix_prod[n-i] = suf

            pref *= nums[i]
            suf *= nums[n-i-1]
        
        for i in range(n):
            out.append(prefix_prod[i] * sufix_prod[i+1])
            
        return out
            