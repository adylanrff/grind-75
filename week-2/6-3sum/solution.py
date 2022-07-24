class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums
        nums.sort()

        results = []
        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            lo = i+1
            hi = len(nums)-1

            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                if current_sum == 0:
                    results.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                elif current_sum < 0:
                    lo += 1
                else:
                    hi -= 1

        return results
