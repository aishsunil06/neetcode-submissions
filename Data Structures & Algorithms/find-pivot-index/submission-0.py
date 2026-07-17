class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0] * n
        suf_sum = [0] * n
        left = 0
        right = 0
        for i in range(n):
            left = left + nums[i]
            right = right + nums[n - 1 - i]
            pref_sum[i] = left
            suf_sum[n-1-i] = right
        for i in range(n):
            if pref_sum[i] - nums[i] == suf_sum[i] - nums[i]:
                return i
        return -1