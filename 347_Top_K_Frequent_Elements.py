from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
        sorted_hm_list=sorted(hm.items(),key=lambda x:x[1],reverse=True)
        #print(hm,sorted_hm_list)
        res=[]
        for i in range(k):
            res.append(sorted_hm_list[i][0])
        return res
