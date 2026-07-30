class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        unique = []

        for num in nums:
            freq[num] += 1
            if freq[num] == 1:
                unique.append(num)
        
        unique.sort(key = lambda n : freq[n])
        return unique[-k:]