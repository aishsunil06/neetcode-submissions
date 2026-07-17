class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in my_hash:
                return [my_hash[needed], i]
            my_hash[nums[i]] = i
        return []
