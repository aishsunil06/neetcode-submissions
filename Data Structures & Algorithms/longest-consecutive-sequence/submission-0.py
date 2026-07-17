class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_hash = {}
        for i in range(len(nums)):
            if nums[i] in my_hash:
                continue
            my_hash[nums[i]] = i
        
        starts = set()
        for num in nums:
            if num - 1 not in my_hash:
                starts.add(num)
            
        best = 0
        for start in starts:
            num = start
            count = 1
            done = False
            while not done:
                if num + 1 in my_hash:
                    count +=1
                    num += 1
                else:
                    best = max(best, count)
                    done = True
        return best