# Last updated: 7/1/2025, 12:33:13 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']


        right, left = 0, len(s) - 1
        result = "" 

        s = list(s)

        while right < left:
            while right < left and s[right].lower() not in vowels:
                right+=1
            while left > right and s[left].lower() not in vowels:
                left-=1
            s[left], s[right] = s[right], s[left]

            right+=1
            left-=1

        
        return "".join(s)



        #order_of_apperance = []
        #
        #for letter in s:
#
        #    lower_cased = letter.lower()
#
        #    if lower_cased not in vowels:
        #        continue
#
        #    order_of_apperance.append(letter)
#
        #vowels_reversed = order_of_apperance[::-1]
#
        ##print(f'order {order_of_apperance}')
        ##print(f'reversed {vowels_reversed}')
#
#
        #vowel_count = 0        
        #result = ""
        #for position, letter in enumerate(s):
        #    
        #    lower_cased = letter.lower()
#
        #    
#
        #    if lower_cased not in vowels:
        #        result+=letter
        #    else:
        #        #print('ere')
        #        result+= vowels_reversed[vowel_count]
        #        
        #        #print(result, vowels_reversed[vowel_count],  vowel_count)
        #        vowel_count+=1
#
        #return result
        #    