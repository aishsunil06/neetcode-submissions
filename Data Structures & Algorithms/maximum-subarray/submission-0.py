import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -math.inf
        run_sum = 0

        if len(nums) == 0:
            return 0

        for num in nums:
            run_sum += num
            max_so_far = max(run_sum, max_so_far)
            if run_sum < 0:
                run_sum = 0
        return max_so_far