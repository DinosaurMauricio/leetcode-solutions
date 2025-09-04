# Last updated: 7/1/2025, 12:33:08 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_number_of_vowels = 0

        # vowel_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        vowels = ["a", "e", "i", "o", "u"]

        current_string = s[0:k]

        for letter in current_string:
            if letter in vowels:
                max_number_of_vowels += 1

        if max_number_of_vowels == k:
            return k

        i = 1
        current = max_number_of_vowels

        while i + k - 1 < len(s):
            current_string = s[i : i + k]

            if s[i - 1] in vowels:
                max_number_of_vowels -= 1

            if current_string[-1] in vowels:
                max_number_of_vowels += 1

            if max_number_of_vowels == k:
                return max_number_of_vowels
            elif current < max_number_of_vowels:
                current = max_number_of_vowels

            i += 1
            # print(current_string)

        return current