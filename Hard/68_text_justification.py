"""
68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you
can in each line. Pad extra spaces ' ' when necessary so that each line has exactly
maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number
of spaces on a line does not divide evenly between words, the empty slots on the left will
be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted
between words.

Note:
    - A word is defined as a character sequence consisting of non-space characters only.
    - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    - The input array words contains at least one word.
"""

"""
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
    "This    is    an",
    "example  of text",
    "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]

Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last
line must be left-justified instead of fully-justified. Note that the second line is also 
left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]
"""

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        current_line_words = []
        current_line_length = 0
        
        for word in words:
            # if adding in current word into existing word line would exceed max width
            if current_line_length + len(word) + len(current_line_words) > maxWidth:
                # calculating available whitespaces
                spaces_to_fill = maxWidth - current_line_length
                gap_count = len(current_line_words) - 1
                # if no word gaps available because it is a single word
                if gap_count == 0:
                    line = current_line_words[0] + (' '*spaces_to_fill)

                else:
                    # figuring out how to distribute whitespaces evenly
                    base_spaces = spaces_to_fill // gap_count
                    extra_spaces = spaces_to_fill % gap_count

                    line_parts = []
                    # iterating through each word in current_line to evenly distribute spaces
                    for i in range(gap_count):
                        # First append word
                        line_parts.append(current_line_words[i])
                        # For the first extra spaces gaps, add one extra space
                        spaces = base_spaces + (1 if i < extra_spaces else 0)
                        # Then append whitespaces
                        line_parts.append(' '*spaces)
                    # Adding in the last word
                    line_parts.append(current_line_words[-1])
                    line = ''.join(line_parts)
                
                result.append(line)
                # Performing Reset for a new line
                current_line_words = []
                current_line_length = 0

            # else if it has yet to hit maxWidth
            current_line_words.append(word)
            current_line_length += len(word)

        # Handling the last line (left-justified)
        if current_line_words:
            line = ' '.join(current_line_words)
            spaces_left = maxWidth - len(line)
            line += ' '*spaces_left
            result.append(line)

        return result