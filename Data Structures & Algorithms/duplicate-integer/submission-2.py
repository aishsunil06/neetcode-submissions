class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}
        for num in nums:
            if num in my_hash:
                return True
            my_hash[num] = True
        return False