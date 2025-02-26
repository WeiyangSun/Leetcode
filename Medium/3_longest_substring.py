"""
3. Longest Substring Without Repeating Characters

Given a string 's', find the length of the longest substring without repeating characters.
"""

"""
Example 1:
Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.
"""


# Double-Pointer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        global_max = 0
        for i in range(len(s)):
            dict = {}
            local_max = 1
            dict[s[i]] = i
            for j in range(i + 1, len(s)):
                if s[j] in dict.keys():
                    break
                dict[s[j]] = j
                local_max += 1
            if local_max > global_max:
                global_max = local_max

        return global_max


# Single-Pointer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}  # Dictionary to store the most recent index of each character
        global_max = 0
        start = 0  # Start of the current window

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                # If the character is repeated and its last occurrence is within the current window
                start = (
                    seen[s[i]] + 1
                )  # Move the start to the next position after the repeated character
            seen[s[i]] = i  # Update the character's most recent index
            global_max = max(
                global_max, i - start + 1
            )  # Calculate the length of the current window

        return global_max
