type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	var sb strings.Builder

	for _, s := range strs {
		sb.WriteString(strconv.Itoa(len(s)))
		sb.WriteString("#")
		sb.WriteString(s)
	}

	return sb.String()
}

func (s *Solution) Decode(encoded string) []string {
	var result []string
	for i := 0; i < len(encoded); {
		j := i
		for encoded[j] != '#' {
			j++
		}

		length, _ := strconv.Atoi(encoded[i:j])

		i = j + 1
		result = append(result, encoded[i:i+length])

		i = i + length
	}
	return result
}
