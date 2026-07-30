class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
            
        n = len(pairs)
        out = [pairs.copy()]
        for index in range(1, n):
            insert = index - 1
            cur = pairs[index]

            while insert >= 0 and pairs[insert].key > cur.key:
                pairs[insert + 1] = pairs[insert]
                insert -= 1
            
            pairs[insert + 1] = cur
            out.append(pairs.copy())

        return out