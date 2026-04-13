class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = buy day, 0
        # right = sell day, 1

        # if right < left, update the buy day
        # if left > right, calculate the profit

        left = 0
        right = 1
        max_profit = 0

        while left < right and right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]

            if sell_price > buy_price:
                max_profit = max(sell_price - buy_price, max_profit)
                right += 1
            else:
                left = right
                right = left + 1
        
        return max_profit