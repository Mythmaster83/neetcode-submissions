class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while right - left > 0:
            height = min(heights[left], heights[right])
            if height * (right-left) > max_area:
                max_area = height*(right-left)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_area