class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        rez = 0

        for i in range(len(heights)):
            left = i - 1
            right = i + 1
            cnt = 1
            while left >= 0 and heights[i] <= heights[left]:
                cnt += 1
                left -= 1
            while right <= (len(heights) - 1) and heights[i] <= heights[right]:
                cnt += 1
                right += 1
            rez = max(rez, cnt * heights[i])
        return rez