# Last updated: 7/1/2025, 12:33:19 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        go_right = 0
        go_left = len(height) - 1
    
        areas = []
        while go_right < go_left or go_left > go_right:
            left_pipie_height = height[go_right]
            right_pipe_height = height[go_left]
    
            # highest_pipe = max(left_pipie_height, right_pipe_height)
            lowest_pipe = min(left_pipie_height, right_pipe_height)
    
            b = go_left - go_right
            h = lowest_pipe  # because if we choose the highest it would fall
    
            area = b * h
            areas.append(area)
    
            if left_pipie_height < right_pipe_height:
                go_right += 1
            else:
                go_left -= 1
    
        return max(areas)