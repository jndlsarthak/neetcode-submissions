class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     s=""
    #     for i in range(len(strs)-1):
    #         s = s + strs[i] + ","
    #     return s

    # def decode(self, s: str) -> List[str]:
    #     strs = s.split(",")
    #     return strs[:-1]

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s = s + i + '..'
        return s

    def decode(self, s: str) -> List[str]:
        strs = s.split("..")
        return strs[:-1]