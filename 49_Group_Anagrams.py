class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            i_sorted=''.join(sorted(i))
            if i_sorted in hm:
                hm[i_sorted].append(i)
            else:
                hm[i_sorted]=[i]
        return hm.values()
