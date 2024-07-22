#standard code:
class Solution:
    def maxProfit(self,prices):
        left = 0
        right = 1 
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
    

#Simplified code: 
class Solution:
    def maxProfit(self,prices):
        a=prices
        mini=a[0];profit=0
        for i in range(1,len(prices)):
            profit=max(profit,a[i]-mini)
            mini=min(mini,a[i])
        return profit