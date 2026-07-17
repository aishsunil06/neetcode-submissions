import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        print("decode")
        return json.loads(s)
