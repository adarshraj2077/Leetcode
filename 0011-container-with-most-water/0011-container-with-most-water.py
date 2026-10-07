class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0

        while i<j:
            water_height = min(height[i],height[j])
            width = j-i

            curr_area = water_height * width

            if curr_area>max_area:
                max_area = curr_area
            
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
            
        return max_area