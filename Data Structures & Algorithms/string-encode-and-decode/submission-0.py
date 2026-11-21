class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result
    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                j = s.find("#",i)
                size = int(s[i:j])
                word = s[j+1 : j+1+size]
                res.append(word)
                i = j+1+size
            return res
        
