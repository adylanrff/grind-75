# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        
        while lo < hi:
            mid = (lo + hi) // 2
            is_bad_version = isBadVersion(mid)
            if is_bad_version:
                hi = mid
            else:
                lo = mid+1
        
        return lo