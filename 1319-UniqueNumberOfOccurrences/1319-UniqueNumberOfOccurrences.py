# Last updated: 7/7/2025, 7:51:30 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = {}

        for num in arr:
            if num in dict_arr:
                dict_arr[num] += 1
            else:
                dict_arr[num] = 1

        number_of_values = len(set(dict_arr.values()))
        ocurrances = len(dict_arr.values())

        return number_of_values == ocurrances