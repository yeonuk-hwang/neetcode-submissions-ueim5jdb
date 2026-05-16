func maxArea(heights []int) int {
	// area = width * min(leftHeight, rightHeight)
	// it only increases when you move the smaller part to the next
	// so, there is only chance to increase area 
	// that you move the smallest height to the next

	left, right := 0, len(heights) - 1
	var maxArea int
	for left < right {
		leftHeight := heights[left]
		rightHeight := heights[right]
		width := right - left
		area := width * min(leftHeight, rightHeight)
		maxArea = max(maxArea, area)

		if leftHeight > rightHeight {
			right--
		} else {
			left++
		}
	}
	return maxArea
}
