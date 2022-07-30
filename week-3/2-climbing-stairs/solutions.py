class Solution:
    dp = {}

    def climbStairs(self, n: int) -> int:
        return self.top_down_dp(n)

    def top_down_dp(self, n):
        if n == 0:
            return 1

        if n == -1:
            return 0

        if self.dp.get(n):
            return self.dp.get(n)

        res = self.top_down_dp(n-1) + self.top_down_dp(n-2)
        self.dp[n] = res

        return self.dp[n]
