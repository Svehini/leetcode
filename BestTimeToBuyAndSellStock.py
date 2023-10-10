class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggestProfit = 0
        skipUntil = -1
        for i in range(0, len(prices)-1):
            if i >= skipUntil:
                for n in range(i+1, len(prices)):
                    diff = prices[n] - prices[i]
                    if diff <= 0:
                        skipUntil = n
                        break
                    if diff > biggestProfit:
                        biggestProfit = diff
        return biggestProfit
