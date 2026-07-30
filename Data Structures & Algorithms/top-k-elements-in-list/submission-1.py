class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        seen = set()
        unique = []

        for num in nums:
            if num not in seen:
                seen.add(num)
                unique.append(num)
            count[num] += 1
        
        unique.sort(key = lambda n : count[n], reverse = True)
        return unique[:k]
