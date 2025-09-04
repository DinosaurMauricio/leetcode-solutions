# Last updated: 7/1/2025, 12:33:04 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums) - 1
        counter = 0

        available = {}
        for num in nums:
            if num not in available:
                available[num] = 1
            else:
                available[num] += 1
                
        while i < len(nums):
            r = k - nums[i]

            if r in available and available[r] > 0:
                available[r] -= 1
                if available[nums[i]] > 0:
                    available[nums[i]] -= 1
                    counter += 1
                else:
                    available[r] += 1
            i += 1
        return counter