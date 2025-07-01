# Last updated: 7/1/2025, 12:33:07 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 1 and len(str2) == 1:
            return str1

        smallest_string = min([str1, str2], key=len)
        largest_string = str2 if len(str2) >= len(str1) else str1
        result = ""
        n=len(smallest_string)

        while n > 0:

            strings_array = [smallest_string[i : i + n] for i in range(0, len(smallest_string), n)]


            target = strings_array[0]

            # if the target doesnt fit why even bother?
            if len(str1) % len(target) != 0 or  len(str2) % len(target)  != 0:
                #n+=1
                n-=1
                continue

            check_strings = [target == s for s in strings_array]

            if False in check_strings:
                #n+=1
                n-=1
                continue

            strings_array = [largest_string[i : i + n] for i in range(0, len(largest_string), n)]
            check_strings = [target == s for s in strings_array]

            #print(target)
            #print(strings_array)
            #print(check_strings)
            if False in check_strings:
                #n+=1
                n-=1
            else:
                result = target
                #continue
                break


        return result


        
        