from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map_s = defaultdict(int)
        char_map_t = defaultdict(int)
        
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        for c in s:
            char_map_s[c] += 1
        
        for c in t:
            char_map_t[c] += 1
                
        for c in alphabets:
            if char_map_s[c] != char_map_t[c]:
                return False
        
        return True