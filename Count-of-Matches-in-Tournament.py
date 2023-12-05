class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches_played = 0
        while (n > 1):
            if n % 2 == 0:
                for i in range(round(n / 2)):
                    matches_played += 1
                n = n / 2
            else:
                for i in range(round((n - 1) / 2)):
                    matches_played += 1
                n = ((n - 1) / 2) + 1
        return matches_played


hello = Solution()
print(hello.numberOfMatches(7))
