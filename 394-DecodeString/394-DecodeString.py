# Last updated: 7/13/2025, 8:01:00 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for value in s:
            if value == "]":
                code = ""
                total_num = ""

                while stack[-1] != "[":
                    code = stack.pop() + code

                stack.pop()  # get rid of '['

                while stack and stack[-1].isdigit():
                    total_num = stack.pop() + total_num

                stack.append(int(total_num) * code)

            else:
                stack.append(value)
        return "".join(stack)