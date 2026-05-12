class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for i in range(len(strs)):
            es+= str(len(strs[i])) + "#" + strs[i]
        return es 
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        i, res = 0, []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res 
            


        
