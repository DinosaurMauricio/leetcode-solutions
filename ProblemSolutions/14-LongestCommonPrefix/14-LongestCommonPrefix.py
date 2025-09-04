# Last updated: 7/1/2025, 12:33:17 PM


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        gt = ""

        min_length = min([len(v) for v in strs])

        i = 0
        #while i < min_length:
        #    self.gt += strs[0][1]
            #self.stack.append(strs[0][i])
        #    i+=1

        for i in range(0, min_length):
            gt = gt + strs[0][i]


        j = 1
        
        num_correct_letters = []
        while j < len(strs):
            word = strs[j]
            correct = 0
            for position_letter in range(0, min_length):
                letter = word[position_letter]
                correct_letter = gt[position_letter]
                #print(letter, correct_letter, letter == correct_letter)

                if letter == correct_letter:
                    correct+=1
                    #print(correct)
                    continue
                else:
                    break
                
            num_correct_letters.append(correct)


            j+=1                                


            #for position_letter in range()
            #self.copy_stack = self.stack.copy()
            
            #print("--------------------------------")
            #for position_letter in range(min_length - 1, -1, -1):
            #    
            #    if self.copy_stack:
            #        letter = word[position_letter]
            #        on_stack_letter = self.copy_stack.pop()
#
            #        print(letter, on_stack_letter, self.copy_stack, self.stack)
            #        if letter == on_stack_letter:
            #            continue
            #        else:
            #            self.stack.pop()
            #            min_length-=1


                    
               # else:
                 #   return ""
            #j+=1

        #print(num_correct_letters)

        return gt[:min(num_correct_letters)] if num_correct_letters else ""

        