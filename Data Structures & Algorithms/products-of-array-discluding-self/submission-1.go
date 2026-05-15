func productExceptSelf(nums []int) []int {
	n := len(nums)
	// prefix slice: value of i is the product of all left elements of i
	prefix := make([]int, n)
	// suffix slice: value of i is the product of all right elements of i
	suffix := make([]int, n)
	// result slice: value of i is product of all except self
	result := make([]int, n)

	prefix[0] = 1
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] * nums[i-1]
	}

	suffix[n-1] = 1
	for i := n - 2; i >= 0; i-- {
		suffix[i] = suffix[i+1] * nums[i+1]
	}

	for i := range result {
		result[i] = prefix[i] * suffix[i]
	}

	return result
}