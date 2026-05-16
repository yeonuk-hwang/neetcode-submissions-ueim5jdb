func maxProfit(prices []int) int {
	// sliding window
	// buy = index 0
	// sell = index 1
	// if current sell is less than buy, 
	// then move the buy to the sell
	// then move the sell to buy + 1
	// calculate the profit and reassign the maxProfit if it exceeds the current max profit

	n := len(prices)
	left, right := 0, 1
	var maxProfit int

	for right < n {
		buy := prices[left]
		sell := prices[right]

		if buy > sell {
			left = right
			right = right + 1
			continue
		}

		profit := sell - buy
		maxProfit = max(maxProfit, profit)
		right += 1
	}

	return maxProfit
}
