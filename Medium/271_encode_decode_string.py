"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is
then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
    return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);
and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.
You are not allowed to solve the problem using any serialize methods (such as eval).
"""

"""
Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2
Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for string in strs:
            encoded.append(f"{len(string)}#{string}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        read_pointer = 0
        n = len(s)

        while read_pointer < n:
            write_pointer = read_pointer
            while s[write_pointer] != "#":
                write_pointer += 1
            length_of_string = int(s[read_pointer:write_pointer])
            start_of_string = write_pointer + 1  # have to account for digit of length
            result.append(s[start_of_string : start_of_string + length_of_string])
            read_pointer = start_of_string + length_of_string
        return result


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for string in strs:
            encoded.append(f"{len(string)}#{string}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        start_pointer = 0
        n = len(s)
        length_of_word = 0

        while start_pointer < n:
            if s[start_pointer] == "#":
                start_pointer += 1
                length_of_word = 0

            if s[start_pointer].isdigit():
                length_of_word = length_of_word * 10 + int(s[start_pointer])
                start_pointer += 1
                continue

            word = s[start_pointer : start_pointer + length_of_word]
            result.append(word)
            start_pointer += length_of_word
        return result
