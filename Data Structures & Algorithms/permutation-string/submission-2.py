class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
            
        count = defaultdict(int)
        check = defaultdict(int)

        for i in range(m):
            check[s2[i]] += 1
            count[s1[i]] += 1
        print(count)
        for i in range(n - m):
            if check == count:
                return True
            
            check[s2[i]] -= 1
            if not check[s2[i]]:
                del check[s2[i]]

            check[s2[i + m]] += 1

        return check == count