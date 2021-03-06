class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if(length==0):
            return 0
        i=0;j=1;l=1
        while(j!=length):
            if(s[j] in s[i:j]):
                l=max(j-i,l)
                i+=s[i:j].index(s[j])+1
            else:
                j+=1;
        return max(l,j-i)
