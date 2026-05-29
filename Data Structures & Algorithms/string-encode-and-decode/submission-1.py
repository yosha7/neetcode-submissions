class Solution:

    def encode(self, strs: List[str]) -> str:
        i=0
        s=""
        for word in strs:
            l=len(word)
            s=s+str(l)+'#'+word
        return s


    def decode(self, s: str) -> List[str]:
        i=0
        strs=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            strs.append(s[j+1:j+1+l])
            i=j+1+l
        return strs
        
