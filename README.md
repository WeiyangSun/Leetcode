# Project Title

LeetCode Solutions

---

## Description

This repository contains my personal solutions to various LeetCode problems. I built this project primarily to practice and improve my data structures and algorithms knowledge. Each solution is accompanied with a brief explanation of the approach taken, if it isn't intuitive. By sharing these solutions, I hope to help others who may be struggling with similar problems and also document my learning journey.

Through this project, I learned:
- How to systematically approach coding problems
- The importance of time and space complexity analysis
- Different algorithmic paradigms like dynamic programming, greedy strategies, backtracking, and more

---

## Features

- **Organized by Difficulty**: Solutions are categorized into Easy, Medium, and Hard folders for ease of navigation.
- **Detailed Explanations**: Each solution file contains an overview of the approach, potential optimizations, and complexity analysis.
- **Multiple Approaches**: Some problems have different levels of solutions.
- **Sample Test Cases**: Included in each solution (where applicable) to demonstrate usage and correctness.

<details>
  <summary>Example Screenshot / Code Snippet</summary>

  ```python
  # Example solution for a LeetCode problem:
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          store = {}
          for i, num in enumerate(nums):
              complement = target - num
              if complement in store:
                  return [store[complement], i]
              store[num] = i
          return []