# Last updated: 7/1/2025, 12:33:23 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            temp = num
            for j, num in enumerate(nums):
                if i == j:
                    continue
                
                if temp + num == target:
                    return [i, j]
