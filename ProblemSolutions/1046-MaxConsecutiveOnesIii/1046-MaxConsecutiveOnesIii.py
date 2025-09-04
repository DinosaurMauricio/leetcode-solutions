# Last updated: 7/1/2025, 3:55:07 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        remaining_ones = k
        left_index = 0
        max_solution = -1

        for right_index, value in enumerate(nums):

            if value == 0:
                remaining_ones -= 1
                while remaining_ones < 0:
                    left_index += 1
                    if nums[left_index - 1] == 0:
                        remaining_ones += 1

            if remaining_ones >= 0:
                temp_sol = right_index - left_index + 1
                max_solution = temp_sol if temp_sol > max_solution else max_solution

        return max_solution