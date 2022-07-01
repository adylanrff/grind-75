from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for idx, num in enumerate(nums):
            nums_map[num] = idx
        
        print(nums_map)
        for idx, num in enumerate(nums):
            if nums_map.get(target-num) != None and nums_map.get(target-num) != idx:
                return idx, nums_map.get(target-num)
        