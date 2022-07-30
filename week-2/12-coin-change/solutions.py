class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        return self.compute_result(coins, amount, {})

    def compute_result(self, coins, rem, count):
        if rem < 0:
            return -1

        if rem == 0:
            return 0

        if count.get(rem):
            return count.get(rem)

        min_coins = 2**31
        for c in coins:
            res = self.compute_result(coins, rem-c, count)
            if res != -1 and res < min_coins:  # there is a result and it is less than the current_min_coins
                min_coins = 1 + res

        count[rem] = min_coins if min_coins != 2**31 else -1
        return count[rem]
