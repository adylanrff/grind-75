from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([(sr, sc)])
        current_color = image[sr][sc]
        
        visited = {}
        
        while queue:
            r,c = queue.popleft()
            if visited.get((r,c)):
                continue
            
            image[r][c] = color
            visited[(r,c)] = True            
            
            directions = [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]
            for direction_r, direction_c in directions:
                if 0 <= direction_r < len(image) and 0 <= direction_c < len(image[0]) and image[direction_r][direction_c] == current_color:
                    queue.append((direction_r, direction_c))
                    
        return image
                