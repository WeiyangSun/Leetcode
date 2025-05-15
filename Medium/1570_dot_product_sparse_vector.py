"""
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

- SparseVector(nums) Initializes the object with the vector `nums`
- dotProduct(vec) Compute the dot product between the instance of SparseVector and `vec`

A sparse vector is a vector that has mostly zero values, you should store the sparse vector
efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""

"""
Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8

Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0

Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
"""

from typing import List, Tuple


class SparseVector:
    def __init__(self, nums: List[int]):
        self.data: List[Tuple[int, int]] = [(ix, v) for ix, v in enumerate(nums) if v != 0]

    def dotProduct(self, vec: "SparseVector") -> int:
        first_pointer = 0
        second_pointer = 0
        dot_product = 0

        first_vector = self.data
        second_vector = vec.data

        while first_pointer < len(first_vector) and second_pointer < len(second_vector):
            first_idx, first_val = first_vector[first_pointer]
            second_idx, second_val = second_vector[second_pointer]

            if first_idx == second_idx:
                dot_product += first_val * second_val
                first_pointer += 1
                second_pointer += 1
            elif first_idx < second_idx:
                first_pointer += 1
            else:
                second_pointer += 1

        return dot_product

    def dotProduct_with_Dense(self, dense_vector):
        dot_product = 0
        for idx, val in self.data:
            dot_product += val * dense_vector[idx]
        return dot_product
