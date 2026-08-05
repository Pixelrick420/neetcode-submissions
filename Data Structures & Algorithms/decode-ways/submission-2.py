class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def decode(index: int) -> int:
            if index == n:
                return 1

            if s[index] == '0':
                return 0

            if index in memo:
                return memo[index]

            ways = decode(index + 1)

            if index + 1 < n:
                num = int(s[index:index + 2])
                if num <= 26:
                    ways += decode(index + 2)

            memo[index] = ways
            return ways

        return decode(0)