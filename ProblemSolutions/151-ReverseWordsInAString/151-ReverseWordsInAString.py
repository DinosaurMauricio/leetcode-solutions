# Last updated: 7/1/2025, 12:33:16 PM
class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()

        s = s.split(" ")

        #print(s)
        
        result = [rev.strip() for rev in s[::-1] if rev]

        result = " ".join(result)

        return result