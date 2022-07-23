import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # lets say intervals are [a,b]
        # lets insert first, then merge later 
        result = []
        
        # insert first
        idx_to_insert = bisect.bisect_left(intervals, newInterval)
        inserted_intervals = intervals[:idx_to_insert] + [newInterval] + intervals[idx_to_insert:]  
        
        last_result = None
        idx = 0     
        
        while idx < len(inserted_intervals):
            cur_interval = inserted_intervals[idx]
            
            if last_result == None:
                result.append(cur_interval)
                last_result = result[-1]
            else:
                # check whether last_result can be merged or not with the new result
                if self.is_intersects(last_result, cur_interval):
                    result[-1] = [min(cur_interval[0], last_result[0]), max(cur_interval[1], last_result[1])]
                else:
                    result.append(cur_interval)
                
            last_result = result[-1]
            idx += 1
            
        return result
            
    def is_intersects(self, interval_a, interval_b):
        if interval_a[0] <= interval_b[0] <= interval_a[1]:
            return True
        if interval_b[0] <= interval_a[0] <= interval_b[1]:
            return True
        
        return False
        
        
        