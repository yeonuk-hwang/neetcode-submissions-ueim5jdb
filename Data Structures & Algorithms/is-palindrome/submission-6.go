func isPalindrome(s string) bool {
	rs := []rune(s)
	start, end := 0, len(rs)-1

	for start < len(rs) && end >= 0 {
		front := rs[start]
		if !isAlphaNumeric(front) {
			start++
			continue
		}
		rear := rs[end]
		if !isAlphaNumeric(rear) {
			end--
			continue
		}

		if unicode.ToLower(front) != unicode.ToLower(rear) {
			return false
		}

		start++
		end--
	}

	return true
}

func isAlphaNumeric(ch rune) bool {
	return unicode.IsDigit(ch) || unicode.IsLetter(ch)
}
