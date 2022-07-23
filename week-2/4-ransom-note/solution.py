from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_char_count = Counter(ransomNote)
        magazine_char_count = Counter(magazine)
        
        for char in ransom_note_char_count:
            if magazine_char_count[char] < ransom_note_char_count[char]:
                return False
        
        return True