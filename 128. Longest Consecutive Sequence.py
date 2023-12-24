class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        max1=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                cnt=1
                while i+cnt in nums:
                    cnt+=1
                if cnt>max1:max1=cnt
        return max1
