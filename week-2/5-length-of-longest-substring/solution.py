class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start_index = 0
        last_char_index = {}

        result = 0
        for window_end_index in range(len(s)):
            current_char = s[window_end_index]
            if current_char in last_char_index:
                window_start_index = max(
                    last_char_index[current_char] + 1, window_start_index)

            result = max(result, window_end_index - window_start_index + 1)
            last_char_index[current_char] = window_end_index

            print(s[window_start_index:window_end_index+1])

        return result
