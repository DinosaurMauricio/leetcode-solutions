# Last updated: 7/1/2025, 12:33:11 PM
class Solution:
    def compress(self, chars: List[str]) -> int:
        pervious_letter = None
        i = 0
        counter = 1  # 1 because the first letter

        while i < len(chars):
            letter = chars[i]

            if i > 0:
                pervious_letter = chars[i - 1]
                # print(pervious_letter)

            if pervious_letter is not None:
                if letter != pervious_letter:
                    skip = 0
                    if counter > 1:
                        while counter > 0:
                            skip += 1
                            attach = counter % 10
                            chars.insert(i, str(attach))
                            counter = counter // 10
                    counter = 1
                    i += skip
                else:
                    counter += 1
                    chars.pop(i)
                    # we remove 1 from i to shift to the removed value
                    i -= 1
            i += 1

        if counter > 1:
            # doesnt need skip bcause its th last thing to do
            while counter > 0:
                attach = counter % 10
                chars.insert(i, str(attach))
                counter = counter // 10

        # print(len(chars))
        # print(chars)

        return len(chars)