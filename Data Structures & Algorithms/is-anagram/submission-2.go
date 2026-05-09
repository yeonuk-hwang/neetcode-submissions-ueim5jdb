func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	counterS := make(map[rune]int, len(s))

	for _, c := range s {
		counterS[c]++
	}

	for _, c := range t {
		counterS[c]--
	}

	for _, v := range counterS {
		if v != 0 {
			return false
		}
	}

	return true
}
