# Last updated: 7/1/2025, 12:33:10 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 if n > 0 else True
        

        free_spaces = 0

        i = 0
        while i < len(flowerbed):

            if flowerbed[i] == 1: # we don't care about the next space bcz theres a plant before
                i+=1
                continue


            #print(f'f is {i}')

            if i == 0: #fisrt pot
                if flowerbed[i] == 0 and  flowerbed[i+1] == 0:
                    free_spaces+=1
                    flowerbed[i] = 1
            elif i+1 == len(flowerbed): #second pot
                #print(i, len(flowerbed))
                if flowerbed[i] == 0 and  flowerbed[i-1] == 0:
                    free_spaces+=1
                    flowerbed[i] = 1
            else: #current
                if flowerbed[i] == 0 and  flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    #print('here')
                    free_spaces+=1
                    #print(f'freespaces is {free_spaces}')
                    flowerbed[i] = 1

            #print(free_spaces, n, free_spaces>=n)
            if free_spaces >= n:
                return True

            i+=1

        return False
