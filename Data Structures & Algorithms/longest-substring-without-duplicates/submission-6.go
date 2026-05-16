func lengthOfLongestSubstring(s string) int {
	// sliding window with variable size
	// start from 0, 1
	// increase right until it finds duplicate
	// update the maximum value to the larger of the current window size
	// and the existing maximum value

	if len(s) == 0 {
		return 0
	}

	l := 0
	n := len(s)
	cs := make(map[rune]bool, n)
	var longest int

	for r, c := range s {
		// if current right character is already in set
		// move the left pointer to the right until there is no duplicate in set
		// when move the pointer, delete the element in the set
		for cs[c] {
			delete(cs, rune(s[l]))
			l++
		}
		cs[c] = true
		longest = max(r - l + 1, longest)
	}

	return longest
}
