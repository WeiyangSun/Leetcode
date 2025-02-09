"""
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots. Each integer is between
0 and 255 (inclusive) and cannot have leading zeros.

- For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312"
and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by
inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the
valid IP addresses in any order.
"""

"""
Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        
        results = []
        
        def backtracking(start_index, combinations):
            if start_index == len(s) and len(combinations) == 4:
                results.append(".".join(combinations))
                return
            
            for length in range(1, 4):
                if start_index + length > len(s):
                    break

                segment = s[start_index:start_index+length]
            
                if segment[0] == '0' and len(segment) > 1:
                    continue
                
                if int(segment) <= 255:
                    combinations.append(segment)
                    backtracking(start_index+length, combinations)
                    combinations.pop()

        backtracking(0, [])
        return results