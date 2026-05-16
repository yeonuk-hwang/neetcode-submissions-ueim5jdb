func twoSum(numbers []int, target int) []int {
	// using two pointer
	// numbers are sorted in ascending order
	// it means the right number is greater than the left number
	// so I can add leftest + rightest, and if 
	// it is greater than target -> I can decrease the number by moving right pointer to the left
	// it is less than target -> I can increase the number by moving left pointer to the right

	left, right := 0, len(numbers) - 1

	for left < right {
		num := numbers[left] + numbers[right]
		difference := target - num

		if difference == 0 {
			return []int{left + 1, right + 1}
		}

		// target is greater than num
		// so increase the num by moving left pointer to the right
		if difference > 0 {
			left++
			continue
		}

		if difference < 0 {
			right--
			continue
		}
	}

	// unreachable code, because there exists always valid answer
	return []int{}
}
