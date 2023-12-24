class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        max_area=0
        while(i<=j):
            area=(j-i)*min(height[i],height[j])
            if max_area<area: max_area=area
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max_area
            
