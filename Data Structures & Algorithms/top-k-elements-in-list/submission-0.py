class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = list(set(nums))
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        unique.sort(key = lambda n : -counts[n])
        return unique[:k]