# Last updated: 7/1/2025, 12:33:15 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        sufix = [1] * len(nums)

        prefix_counter = 1
        for i in range(len(nums)):
            prefix[i] = prefix_counter
            prefix_counter *= nums[i]

        prefix_counter = 1
        for i in range(len(nums) - 1, -1, -1):
            sufix[i] = prefix_counter
            prefix_counter *= nums[i]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * sufix[i])

        return result