class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff=0
        min_prices=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_prices:
                min_prices=prices[i]
            if prices[i]-min_prices>maxdiff:
                maxdiff=prices[i]-min_prices
        return maxdiff
