func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	counterS := make(map[rune]int, len(s))

	for i, c := range s {
		counterS[c]++
		counterS[rune(t[i])]--
	}

	for _, v := range counterS {
		if v != 0 {
			return false
		}
	}

	return true
}
