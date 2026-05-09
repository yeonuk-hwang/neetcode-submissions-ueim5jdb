func twoSum(nums []int, target int) []int {
    // lookup pairValue, that satisfies pairValue + currentValue = target
	// return the indicies of pairValue and currentValue

	// make a map which is {value: index}
	values := make(map[int]int, len(nums))

	for i, v := range nums {
		// check ok, because map returns zero value, which is integer 0
		// when there is not key in the map
		if pairIndex, ok := values[target - v]; ok {
			return []int{pairIndex, i}
		} 

		values[v] = i
	}

	// dead code, because there exist i and j such that satisfies the condition
	return []int{0, 0}
}
