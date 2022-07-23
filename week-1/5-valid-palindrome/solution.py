class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        lower_s = lower_s.strip(" ")
        
        lower_s = [c for c in lower_s if c.isalnum()]
        
        idx = 0
        last_idx = len(lower_s) - 1
        
        while idx < last_idx and 0 <= idx < len(lower_s) and 0 <= last_idx < len(lower_s):            
            if lower_s[idx] != lower_s[last_idx]:
                return False
            
            idx +=1
            last_idx -= 1
        
        return True
                
        
        
            