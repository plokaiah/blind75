class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm={}
        max_len=0
        slow=0
        for fast in range(len(s)):
            if s[fast] in hm:
                slow=max(slow,hm[s[fast]]+1)
            max_len=max(max_len,fast-slow+1)
            hm[s[fast]]=fast
        return max_len
