class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        for c in s:
            if c not in s_hash:
                s_hash[c] = 1
            else:
                s_hash[c] += 1
        for c in t:
            if c not in s_hash:
                return False
            s_hash[c] -= 1
            if s_hash[c] < 0:
                return False
        return True