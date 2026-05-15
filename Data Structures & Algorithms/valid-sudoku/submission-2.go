func isValidSudoku(board [][]byte) bool {
	// create a set for
	// 1. row
	// 2. column
	// 3. sub-box
	rows := make([]map[byte]bool, 9)
	columns := make([]map[byte]bool, 9)
	boxes := make([]map[byte]bool, 9)

	for i := range 9 {
		rows[i] = make(map[byte]bool, 9)
		columns[i] = make(map[byte]bool, 9)
		boxes[i] = make(map[byte]bool, 9)
	}

	for row := range 9 {
		for col := range 9 {
			val := board[row][col]
			if val == '.' {
				continue
			}
			boxWidth := 3
			boxHeight := 3
			boxesPerRow := 3
			boxIndex := (row/boxWidth)*boxesPerRow + (col / boxHeight)

			if rows[row][val] || columns[col][val] || boxes[boxIndex][val] {
				return false
			}

			rows[row][val] = true
			columns[col][val] = true
			boxes[boxIndex][val] = true
		}
	}

	// row number is index of array -> r
	// column number is index of elements -> c
	// sub-box numnrt is flattened index of r, c
	// r / 3 (the width of box) * 3 (the number of box in a row) + column

	return true
}
