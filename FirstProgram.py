class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

# Test Cases
print(f"Longest Substring for 'abcabcbb': {Solution().lengthOfLongestSubstring('abcabcbb')}") # Expected: 3
print(f"Longest Substring for 'bbbbb': {Solution().lengthOfLongestSubstring('bbbbb')}") # Expected: 1
print(f"Longest Substring for 'pwwkew': {Solution().lengthOfLongestSubstring('pwwkew')}") # Expected: 3
print(f"Longest Substring for '': {Solution().lengthOfLongestSubstring('')}") # Expected: 0
print(f"Longest Substring for 'au': {Solution().lengthOfLongestSubstring('au')}") # Expected: 2