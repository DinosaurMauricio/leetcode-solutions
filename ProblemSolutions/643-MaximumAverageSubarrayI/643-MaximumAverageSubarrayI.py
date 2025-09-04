# Last updated: 7/1/2025, 12:33:09 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)

        pointer = 0
        results = []

        temp_array = nums[:k]
        temp = 0
        for val in temp_array:
            temp += val
        temp_total = temp / k
        results.append(temp_total)

        pointer = k

        #print(pointer, len(nums))
        while pointer < len(nums):
            #print(f'temp is right now {temp}')
            temp+= nums[pointer]
            temp-= nums[pointer - k]

            #print(nums[pointer], nums[pointer - k] - 1, temp)

            temp_total = temp / k
            results.append(temp_total)
            pointer+=1
            #print(f'at the end pointer {pointer} and len(nums) {len(nums)}')


            #temp  = 0
            #temp_array = nums[pointer:pointer +k]
#
            #if len(temp_array) != k:
            #    break
            ##print(f'temp array is {temp_array}')
            #for val in temp_array:
            #    temp += val
            #temp/=k
            #results.append(temp)
            #pointer+=1

        #print(results)

        return max(results)

            