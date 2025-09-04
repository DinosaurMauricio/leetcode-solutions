# Last updated: 7/1/2025, 12:33:21 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) == 1:
            return 1


        result_value = -1 

        for index in range(0, len(s)):
            substring = s[index]


            for index_j in range (index+1, len(s)):
                next_letter = s[index_j]

                #print(substring, next_letter)

                if next_letter in substring:
                    current_length = len(substring)
                    if current_length > result_value:
                        result_value = current_length

                    break
                substring+= next_letter

                current_length = len(substring)
                if current_length > result_value:
                        result_value = current_length

                #print(substring)
        
        return result_value



        #current_substring = ""
        #result_value = -1 
        #for string_val in s:
        #    #print(f'string val is {string_val}')
        #    #print(current_substring)
        #    
        #    if string_val in current_substring:
        #        current_length = len(current_substring)
        #        if current_length > result_value:
        #            result_value = current_length
        #        current_substring = string_val
#
        #    current_substring+= string_val
        #    current_length = len(current_substring)
        #    if current_length > result_value :
        #        result_value = current_length
#
        #return result_value