class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        n = len(nums)

        for right in range(n):
            heapq.heappush(heap, (-nums[right], right))
            if right >= (k - 1):
                while heap[0][1] <= (right - k):
                    heapq.heappop(heap)
                output.append(-heap[0][0])
            
        return output