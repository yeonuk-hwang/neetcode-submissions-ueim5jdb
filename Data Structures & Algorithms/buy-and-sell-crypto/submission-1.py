class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # save low_value, and save max_value
        # if the current_value is less than low_value, set this as an low_value
        # calculate the profit (current_value - low_value), and if it is greater than the current maxium profit,
        # set it as the profit

        low_value = prices[0];
        current_maximum_profit = 0

        for price in prices:
            profit = price - low_value
            current_maximum_profit = max(profit, current_maximum_profit)
            low_value = min(price, low_value)
        
        return current_maximum_profit

            

