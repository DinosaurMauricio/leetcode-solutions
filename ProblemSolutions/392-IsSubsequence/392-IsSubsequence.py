# Last updated: 7/1/2025, 12:33:12 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s = list(s)

        for letter in t:
            if s:
                if s[0] == letter:
                    s.pop(0)
                    if not s:
                        return True

            else:
                return True

        return False