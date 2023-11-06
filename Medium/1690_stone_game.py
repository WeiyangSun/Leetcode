"""
1690. Stone Game VII

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the
leftmost stone or the rightmost stone from the row and receive points equal to the sum of the 
remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), 
so he decided to minimize the score's difference. 
Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the 
ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.
"""

"""
Example 1:
Input: stones = [5,3,1,4,2]
Output: 6

Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122
"""

"""
Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""

class RecursiveSolution:
    def stoneGameVII(self, stones: list(int)) -> int:

        N = len(stones)
        def recursive_helper(i, j) -> None:
            #Base Case - Ran out of Options:
            if i > j: return 0
            
            total = sum(stones[i:j+1]) #j+1 because of Python indexing

            return total - min(stones[i]+recursive_helper(i+1,j), stones[j]+recursive_helper(i,j-1))
        
        return recursive_helper(0, N-1) #N-1 because of python zero-indexing

from itertools import accumulate 
class RecursiveMemoSolution:
    def stoneGameVII(self, stones: list(int)) -> int:
        
        N = len(stones)
        S = [0] + list(accumulate(stones))
        
        @lru_cache(1000)
        def recursive_helper(i: int, j: int) -> None:
            #Base Case
            if i > j: return 0

            total = S[j+1] - S[i]

            return total - min(stones[i]+recursive_helper(i+1,j), stones[j]+recursive_helper(i,j-1))
        
        return recursive_helper(0, N-1)
    
class DynamicMemoSolution:
    def stoneGameVII(self, stones: list(int)) -> int:

        N = len(stones)
        S = [0] + list(accumulate(stones))
        memo = [[0] * N for _ in range(N)]

        def dfs(left_pointer: int, right_pointer: int) -> None:
            #Base Case - No more Options Left:
            if left_pointer == right_pointer: return 0

            #Checking Memo if Value exists already:
            if memo[left_pointer][right_pointer] == 0:
                range_sum = S[right_pointer+1] - S[left_pointer]
                memo[left_pointer][right_pointer] = max(range_sum-stones[left_pointer]-dfs(left_pointer+1, right_pointer),
                                                        range_sum-stones[right_pointer]-dfs(left_pointer, right_pointer-1))
            return memo[left_pointer][right_pointer]
        
        return dfs(0, N-1)
    
