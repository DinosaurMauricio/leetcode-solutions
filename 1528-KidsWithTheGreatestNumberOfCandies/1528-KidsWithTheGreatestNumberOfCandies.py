# Last updated: 7/1/2025, 12:33:06 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most_candies = max(candies)

        results = [extraCandies + kid_candies >= most_candies for kid_candies in candies]

        return results
        