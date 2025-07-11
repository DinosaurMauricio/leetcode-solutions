# Last updated: 7/11/2025, 5:38:05 PM
from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for letter in s:
            if letter == "*":
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)