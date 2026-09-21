class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        if s == "":
            return 0
        my_hash = {s[l] : 1}
        length = max_len = 1
        while l <= r and r < len(s) - 1:
            r += 1
            length += 1
            # aaaaaaa wxwxyz a
            while s[r] in my_hash:
                del my_hash[s[l]]
                l += 1 #l=0 r=1 h=a length=1
                length -= 1
            my_hash[s[r]] = 1
            max_len = max(max_len, length)
        return max_len