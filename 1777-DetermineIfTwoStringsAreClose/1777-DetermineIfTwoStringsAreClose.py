# Last updated: 7/8/2025, 4:05:45 PM
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        dicts1, dicts2 = {}, {}
        for word in word1:
            dicts1[word] = dicts1.get(word, 0) + 1

        for word in word2:
            dicts2[word] = dicts2.get(word, 0) + 1

        if len(dicts1.keys() - dicts2.keys()) != 0:
            return False  # there are elements that dont exit in one, so its impossible to rebuild the string

        freq_counts = {}

        for v in dicts2.values():
            freq_counts[v] = freq_counts.get(v, 0) + 1

        for letter_count in dicts1.values():
            if letter_count not in freq_counts.keys() or freq_counts[letter_count] <= 0:
                return False
            freq_counts[letter_count] -= 1

        return True