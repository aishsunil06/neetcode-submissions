class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        water = [0] * len(height)

        for i in range(1, len(height)):
            j = len(height) - i - 1
            max_left[i] = max(max_left[i-1], height[i-1])
            max_right[j] = max(max_right[j+1], height[j+1])
        
        total_water = 0
        for i in range(len(height)):
            water[i] = max(min(max_left[i], max_right[i]) - height[i], 0)
            total_water += water[i]

        return total_water
        