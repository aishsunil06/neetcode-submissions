class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = max_len = 0
        my_hash = {}
        for r in range(len(s)):
            # aaaaaaa wxwxyz a
            if s[r] in my_hash and my_hash[s[r]] >= l:
                l = my_hash[s[r]] + 1
            my_hash[s[r]] = r
            max_len = max(max_len, r - l + 1)
        return max_len