from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distance = [[2**31 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        queue = deque()
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for i,row in enumerate(mat):
            for j, col in enumerate(row):
                if col == 0:
                    distance[i][j] = 0
                    queue.append((i,j))
        
        while queue:
            i,j = queue.popleft()
            for di,dj in directions:
                new_i = i+di
                new_j = j+dj
                
                if 0 <= new_i < len(mat) and 0 <= new_j < len(mat[0]):
                    if distance[new_i][new_j] > distance[i][j]+1:
                        distance[new_i][new_j] = distance[i][j]+1
                        queue.append((new_i,new_j))
            
        
            
        return distance