from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = defaultdict(int)

        for c in s:
            char_map[c] += 1

        has_odd_char_count = 0

        result = 0
        for k in char_map:
            count = char_map[k] // 2 * 2
            result += count

            if char_map[k] % 2 == 1:
                has_odd_char_count = 1

        return result + has_odd_char_count
