"""
15. 3Sum

Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

"""
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        negative_numbers = sorted([num for num in nums if num < 0])
        positive_numbers = sorted([num for num in nums if num > 0])
        neutral_numbers = [num for num in nums if num == 0]
        plausible_solutions = set()
        
        positive_set = set(positive_numbers)
        negative_set = set(negative_numbers)

        #Rule 1: 2 negative number 1 positive number
        for i in range(len(negative_numbers)):
            for j in range(i+1, len(negative_numbers)):
                needed_positive_number = -(negative_numbers[i] + negative_numbers[j])
                if needed_positive_number in positive_set:
                    triplet = tuple(sorted([negative_numbers[i], negative_numbers[j], needed_positive_number]))
                    plausible_solutions.add(triplet)
                
        #Rule 2: 2 positive number 1 negative number
        for i in range(len(positive_numbers)):
            for j in range(i+1, len(positive_numbers)):
                needed_negative_number = -(positive_numbers[i] + positive_numbers[j])
                if needed_negative_number in negative_set:
                    triplet = tuple(sorted([positive_numbers[i], positive_numbers[j], needed_negative_number]))
                    plausible_solutions.add(triplet)

        #Rule 3: 1 positive number 1 negative number 1 neutral number
        if neutral_numbers:
            for each_positive_number in positive_set:
                if -each_positive_number in negative_set:
                    plausible_solutions.add((-each_positive_number, 0 , each_positive_number))

        #Rule 4: 3 neutral number
        if len(neutral_numbers) >= 3:
            plausible_solutions.add((0, 0, 0))

        return [list(triplet) for triplet in plausible_solutions]

sol = Solution()
print(sol.threeSum(nums=[-1,0,1,2,-1,-4]))