# Last updated: 7/3/2025, 2:34:07 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        postfix_sum = [0]

        temp = 0
        for n in range(0, len(nums) - 1):
            temp += nums[n]
            prefix_sum.append(temp)

        temp = 0
        for n in range(len(nums) - 1, 0, -1):
            temp += nums[n]
            postfix_sum.append(temp)

        postfix_sum.reverse()

        for i in range(len(prefix_sum)):
            if prefix_sum[i] == postfix_sum[i]:
                return i

        return -1