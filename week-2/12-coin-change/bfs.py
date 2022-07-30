from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        return self.compute_result(coins, amount)

    def compute_result(self, coins, amount):
        queue = deque([amount])
        steps = 0
        visited = {}
        while queue:
            size = len(queue)
            while size > 0:
                cur_amount = queue.popleft()
                size -= 1
                if cur_amount == 0:
                    return steps
                for c in coins:
                    if cur_amount - c >= 0 and not visited.get(cur_amount-c):
                        queue.append(cur_amount-c)
                        visited[cur_amount-c] = True
            steps += 1

        return -1
