class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}
        result = []
        for string in strs:
            key = tuple(sorted(string))
            if key not in my_hash:
                my_hash[key] = len(result)
                result.append([])
            result[my_hash[key]].append(string)
        return result
