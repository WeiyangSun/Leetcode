"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there
is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

"""
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"

Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""

Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target_dict = Counter(t)
        target_unique = len(target_dict)
        
        # Counters for sliding windows
        left = 0
        sliding_dict = {}
        sliding_unique = 0
        
        # Index for results
        result_length = float('inf')
        result_start = 0
        
        for right, char in enumerate(s):
            
            # Recording character into sliding_dict to capture what sliding window has come across
            sliding_dict[char] = sliding_dict.get(char, 0) + 1
            
            # If character is in target and frequency matches between sliding window and target
            if char in target_dict and sliding_dict[char] == target_dict[char]:
                # unique characters in sliding windows increases by 1
                sliding_unique += 1
            
            # Trying to shrink window from left as long as we have all target required
            while sliding_unique == target_unique:
                # Shrink sliding window
                window_size = right - (left + 1)
                if window_size < result_length:
                    result_length = window_size
                    result_start = left
                
                # Character that is about to be removed because of shrinking window
                left_char = s[left]
                sliding_dict[left_char] -= 1
                # If character is in target_dict and we have dropped below target count
                if left_char in target_dict and sliding_dict[left_char] < target_dict[left_char]:
                    sliding_unique -= 1
                
                # Move left pointer forward to shrink window
                left += 1
            
        if result_length == float('inf'):
            return ""
        else:
            return s[result_start: result_start+result_length]