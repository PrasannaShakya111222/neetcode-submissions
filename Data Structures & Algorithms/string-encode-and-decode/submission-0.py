class Solution:
    def encode(self, strs: List[str]) -> str:
        result =""
        for word in strs:
            result +=str(len(word))+"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        result =[]
        i= 0
        while i < len(s):
            j =i
            while s[j] !="#":
                j += 1
            length = int(s[i:j])
            j +=1
            result.append(s[j:j+length])
            i =j+length
        return result