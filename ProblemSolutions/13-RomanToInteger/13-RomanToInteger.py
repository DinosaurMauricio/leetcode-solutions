# Last updated: 7/1/2025, 12:33:18 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }



        i = 0 
        total = 0

        while i < len(s):
            value = roman_map[s[i]]
            if i + 1 < len(s):
                next_value = roman_map[s[i+1]]

                if value < next_value:
                    total = total + next_value - value
                    i+=2
                    continue
            total+= value
            i+=1
        
        return total