class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                w = j - i
                a = h * w
                if a > max_water:
                    max_water = a
        return max_water

    

        