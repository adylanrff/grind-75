from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = [[False for _ in range(len(grid[0]))]
                  for _ in range(len(grid))]
        queue = deque([])

        fresh_oranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

                if grid[i][j] == 1:
                    fresh_oranges += 1

        print(fresh_oranges)
        minutes = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                cur_i, cur_j = queue.popleft()

                for dir_i, dir_j in directions:
                    next_i = cur_i + dir_i
                    next_j = cur_j + dir_j
                    if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                        if grid[next_i][next_j] == 1:
                            grid[next_i][next_j] = 2
                            fresh_oranges -= 1
                            queue.append((next_i, next_j))

            minutes += 1

        return minutes if fresh_oranges == 0 else -1
