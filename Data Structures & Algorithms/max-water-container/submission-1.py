class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights)):
            l = i
            r = len(heights) - 1
            while l < r:
                a = min(heights[l], heights[r]) * (r - l)
                if a > max_water:
                    max_water = a
                if heights[l] < heights[r]:
                    l += 1
                if heights[l] > heights[r]:
                    r -= 1
                else:
                    l += 1
                    r -= 1
        return max_water

    
    

        