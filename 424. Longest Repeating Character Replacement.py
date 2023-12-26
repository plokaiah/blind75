class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        slow = 0
        max_freq = 0
        res = 0

        for fast in range(len(s)):
            hm[s[fast]] = hm.get(s[fast], 0) + 1
            max_freq = max(max_freq, hm[s[fast]])

            if (fast - slow + 1)   > k+max_freq:
                hm[s[slow]] -= 1
                slow += 1

            res = max(res, fast - slow + 1)

        return res
