class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_hash = {}
        for idx in range(len(numbers)):
            num = numbers[idx]
            if target - num in my_hash:
                return [my_hash[target - num], idx + 1]
            my_hash[num] = idx + 1
        return [0]
        