"""
838. Push Dominoes

There are n dominoes in a line, and we place each domino vertically upright. In the beginning,
we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the
left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the
right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance
of the forces.

For the purpose of this question, we will consider that a falling domino expends no additional force
to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:
- dominoes[i] = 'L', if the i-th domino has been pushed to the left,
- dominoes[i] = 'R', if the i-th domino has been pushed to the right, and
- dominoes[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.
"""

"""
Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"

Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL..
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        right_forces = [float("inf")] * N  # time since last 'R' to the left
        left_forces = [float("inf")] * N  # time since last 'L' to the right

        # Left to Right Pass - Track pushes from 'R'
        force = float("inf")
        for i in range(N):
            if dominoes[i] == "R":  # starts a new rightward push
                force = 0
            elif dominoes[i] == "L":  # blocks rightward push
                force = float("inf")
            else:
                if force != float("inf"):
                    force += 1  # increase distance from last R
            right_forces[i] = force

        # Right to Left Pass - Track pushes from 'L'
        force = float("inf")
        for i in reversed(range(N)):
            if dominoes[i] == "L":
                force = 0
            elif dominoes[i] == "R":
                force = float("inf")
            else:
                if force != float("inf"):
                    force += 1
            left_forces[i] = force

        # Combining
        result = []
        for i in range(N):
            if right_forces[i] < left_forces[i]:
                result.append("R")  # right pushes arrives first
            elif left_forces[i] < right_forces[i]:
                result.append("L")
            else:
                result.append(dominoes[i] if left_forces[i] == float("inf") else ".")
        return "".join(result)


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        A = list("L" + dominoes + "R")
        pointer_A = 0

        for pointer_B in range(1, len(A)):
            if A[pointer_B] == ".":
                continue
            gap = pointer_B - pointer_A - 1
            if gap > 0:
                # if both identified dominoes are the same, then all in the middle should follow
                if A[pointer_A] == A[pointer_B]:
                    for k in range(pointer_A + 1, pointer_B):
                        A[k] = A[pointer_A]
                # both pointers are falling inward
                elif A[pointer_A] == "R" and A[pointer_B] == "L":
                    left, right = pointer_A + 1, pointer_B - 1
                    while left < right:
                        A[left], A[right] = "R", "L"
                        left += 1
                        right -= 1

            pointer_A = pointer_B  # moving forward
        return "".join(A[1:-1])  # removes ends
