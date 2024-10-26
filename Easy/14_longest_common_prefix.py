"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, s: list[str]) -> str:

        # Edge Case
        if not s:
            return ""

        common_prefix = s[0]

        for word in s[1:]:
            while not word.startswith(common_prefix):
                common_prefix = common_prefix[:-1]

            if not common_prefix:
                return ""

        return common_prefix

class Solution:
    def longestCommonPrefix(self, s: list[str]) -> str:

        # Edge Case
        if not s:
            return ""

        min_word_length = min([len(word) for word in s])
        common_prefix = []

        for i in range(min_word_length):
            current_char = s[0][i] #takes first word i-th character
            
            if all(word[i] == current_char for word in s):
                common_prefix.append(current_char)
            else:
                break

        return "".join(common_prefix)

sol = Solution()
print(sol.longestCommonPrefix(s=["flower","flow","flight"]))