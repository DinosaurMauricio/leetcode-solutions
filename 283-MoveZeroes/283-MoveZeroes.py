# Last updated: 7/1/2025, 12:33:14 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i, j = 0, 0

        while i < len(nums) and j < len(nums):
            while nums[i] != 0:
                i += 1
                if i + 1 > len(nums):
                    break
                #print(f"i {i} { j}, num {nums[i]}, boolean i < j {i < j}")

            j = i + 1

            while i < j and j < len(nums) and nums[j] == 0:
                j += 1

            if j + 1 > len(nums):
                break

            # print(i, j)
            if nums[j - 1] == 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

        