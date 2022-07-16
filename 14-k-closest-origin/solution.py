import math
import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points, k):
        left, right = 0, len(points)-1
        pivot_index = len(points)
        
        while pivot_index != k:
            pivot_index = self.partition(points, left, right)
            
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        return points[:k]
    
    def partition(self, points, left, right):
        pivot = self.choose_pivot(points, left, right)
        pivot_distance = self.squared_distance(pivot)
        
        while left < right:
            if self.squared_distance(points[left]) >= pivot_distance:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        if self.squared_distance(points[left]) < pivot_distance:
            left += 1
        
        return left
                
            
        
    def choose_pivot(self, points, left, right):
        return points[left + (right-left) // 2]
    
    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2