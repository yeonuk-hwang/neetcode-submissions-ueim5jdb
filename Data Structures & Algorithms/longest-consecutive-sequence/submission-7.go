func longestConsecutive(nums []int) int {
	// find smallest
	// save number in map
	// start from smallest and lookup consecutive number in map
	// return the result
	// fails, because consecutive number is not always start from smallest

	var smallest int
	set := make(map[int]bool, len(nums))

	for i, v := range nums {
		if i == 0 {
			smallest = v
		}

		smallest = min(smallest, v)
		set[v] = true
	}

	result := 0

	for num := range set {
		if set[num-1] {
			continue
		}

		length := 1
		current := num
		for set[current+1] {
			length++
			current++
		}

		result = max(result, length)
	}

	return result
}
