class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        res = cur_sum

        for idx in range(1, len(nums)):
            cur_sum = max(nums[idx], cur_sum + nums[idx])
            res = max(res, cur_sum)
            
        return res
