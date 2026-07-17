class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in my_hash:
                return [my_hash[need], i]
            my_hash[nums[i]] = i