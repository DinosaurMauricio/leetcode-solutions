# Last updated: 7/3/2025, 12:44:09 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        result = 0

        for g in gain:
            start += g
            result = max(start, result)

        return result