class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        seen = []
        for idx in range(len(nums)):
            num = nums[idx]
            if num in seen:
                continue
            seen.append(num)
            left = idx + 1
            right = len(nums) - 1
            while left < right and left < len(nums) and right > 0:
                current_sum = num + nums[left] + nums[right]
                if current_sum == 0:
                    output.append([num, nums[left], nums[right]])
                    prev = nums[left]
                    while left < len(nums) and prev == nums[left]:
                        left += 1
                    prev = nums[right]
                    while right > 0 and prev == nums[right]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        return output
        