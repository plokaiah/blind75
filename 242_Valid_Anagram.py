class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms={}
        hmt={}
        for i in s:
            hms[i]=hms.get(i,0)+1
        for i in t:
            hmt[i]=hmt.get(i,0)+1
        if hms==hmt:
            return True
        else:
            return False
