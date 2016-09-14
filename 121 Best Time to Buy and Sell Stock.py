class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        
        buy = prices[0]
        sale = 0
        profit = 0
        
        for i in range(len(prices)):
            if prices[i]<=buy:
                buy = prices[i]
            else:
                sale = prices[i]
                if sale-buy > profit:
                    profit = sale-buy
        
        if profit>0:
            return profit
        else:
            return 0
