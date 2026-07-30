class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leftArr, rightArr = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        m, n = len(leftArr), len(rightArr)
        if n < m:
            leftArr, rightArr = rightArr, leftArr
            m, n = n, m
        
        left, right = 0, m - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            leftMin = leftArr[i] if i >= 0 else float('-inf')
            leftMax = leftArr[i + 1] if (i + 1) < m else float('inf')
            rightMin = rightArr[j] if j >= 0 else float('-inf')
            rightMax = rightArr[j + 1] if (j + 1) < n else float('inf')
        
            if leftMin <= rightMax and rightMin <= leftMax:
                if total % 2:
                    return min(leftMax, rightMax)
                return (max(leftMin, rightMin) + min(leftMax, rightMax)) / 2.0
            
            elif leftMin > rightMax:
                right = i - 1
            
            else:
                left = i + 1
        
        return -1
