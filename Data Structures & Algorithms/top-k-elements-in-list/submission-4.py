class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        seen = set()
        uniq = []
        for num in nums:
            count[num] += 1
            if num not in seen:
                uniq.append(num)

            seen.add(num)
        
        uniq.sort(key = lambda n : count[n])
        return uniq[-k:]