# Last updated: 7/1/2025, 12:33:05 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ""

        letter1 =""
        letter2= ""

        i = 0
        while letter1 is not None or letter2 is not None:
            letter1 = word1[i] if i < len(word1) else None
            letter2 = word2[i] if i < len(word2) else None
            
            if letter1:
                result+=letter1
            if letter2:
                result+=letter2

            i+=1
            
        return result


            

