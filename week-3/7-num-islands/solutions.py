class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))]
                   for _ in range(len(grid))]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, visited, i, j)
                    count += 1

        return count

    def dfs(self, grid, visited, i, j):
        stack = [(i, j)]  # start from i,j
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        while stack:
            cur_i, cur_j = stack.pop()
            if visited[cur_i][cur_j] or grid[cur_i][cur_j] == "0":
                continue

            visited[cur_i][cur_j] = True
            for dir_i, dir_j in directions:
                next_i = cur_i+dir_i
                next_j = cur_j+dir_j
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                    if grid[next_i][next_j] == "1":
                        stack.append((next_i, next_j))
