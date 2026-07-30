class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        seen = set()
        for num in nums:
            count[num] += 1
            seen.add(num)
        
        uniq = list(seen)
        uniq.sort(key = lambda n : count[n])
        return uniq[-k:]