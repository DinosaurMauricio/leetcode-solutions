# Last updated: 7/15/2025, 3:22:08 PM
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # This is O(N^2) :( would have been better with queues instead of this approach i took
        n_senate = len(senate)
        r, d = 0, 0
        i, j = 0, 0

        for s in senate:
            if s == "R":
                r += 1
            else:
                d += 1

        senate = list(senate)

        while True:
            if d == 0 or r == 0:
                break

            if senate[i] == "B":
                i = 0 if i + 1 == n_senate else i + 1
                continue

            while j < len(senate):

                j = 0 if j + 1 == len(senate) else j + 1 
                if senate[j] != "B" and senate[j] != senate[i]:
                    break

            if senate[j] == "D":
                d -= 1
            else:
                r -= 1

            senate[j] = "B"

            # if reached max len its the end of the round, so we restart i
            i = 0 if i + 1 == n_senate else i + 1

        result = "Radiant" if r > 0 else "Dire"

        return result