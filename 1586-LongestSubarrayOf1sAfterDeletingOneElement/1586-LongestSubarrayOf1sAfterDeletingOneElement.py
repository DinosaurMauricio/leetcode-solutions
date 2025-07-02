# Last updated: 7/2/2025, 2:46:47 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_index = 0
        # can only remove one so instead just save a boolean
        removed = False
        max_result = -1
        zero_index = -1

        for right_index, val in enumerate(nums):

            if val == 0:
                if not removed:
                    removed = True
                else:
                    left_index = zero_index + 1
                zero_index = right_index

            result = right_index - left_index  # index = 0 so we have to add one

            max_result = max(max_result, result)


        return max_result