# Last updated: 7/4/2025, 12:54:43 PM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        difference_set1 = nums1_set - nums2_set
        difference_set2 = nums2_set - nums1_set

        return [list(difference_set1), list(difference_set2)]