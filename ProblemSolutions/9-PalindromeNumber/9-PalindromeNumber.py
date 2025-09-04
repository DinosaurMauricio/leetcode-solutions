# Last updated: 7/1/2025, 12:33:20 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reversing_num = 0 
        while x > 0:
            reversing_num = reversing_num*10 + x% 10
            x //= 10

        return reversing_num == temp