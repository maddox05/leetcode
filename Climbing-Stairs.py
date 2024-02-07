class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        current = 0
        for i in range(3, n + 1):  # include the last element
            current = a + b
            a, b = b, current
        return current
