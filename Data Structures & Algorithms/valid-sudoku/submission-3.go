func isValidSudoku(board [][]byte) bool {
	// iterate all sudoku cells
	// examine if there is a duplicate in 
	// a row
	// a column
	// a sub-box
	// if there is a duplicate, it means the sudoku is not valid
	// if there is no duplicate, it means the sudoku is valid.

	// to examine duplicate, I need a Set, because I need O(1) look up
	// to iterate all cells, I need to loop all columns in a loop of all rows
	var result bool = true

	rowSet := make([]map[int]struct{}, 9)
	colSet := make([]map[int]struct{}, 9)
	boxSet := make([]map[int]struct{}, 9)
	// the zero value of map is nil, so all the slice elements are nil now
	// to avoid nil dereference panic, initialise all elements with empty map

	for i := range 9 {
		rowSet[i] = make(map[int]struct{}, 9)
		colSet[i] = make(map[int]struct{}, 9)
		boxSet[i] = make(map[int]struct{}, 9)
	}

	for r := range 9 {
		for c := range 9 {
			val := rune(board[r][c])
			if val == '.' {
				continue
			}
			num := int(val - '0')
			boxRow := r / 3
			boxCol := c / 3
			boxIndexInOneDimension := boxRow * 3 + boxCol

			_, isDuplicateInRow := rowSet[r][num]
			_, isDuplicateInCol := colSet[c][num]
			_, isDuplicateInBox := boxSet[boxIndexInOneDimension][num]

			if isDuplicateInRow || isDuplicateInCol || isDuplicateInBox {
				result = false
			}

			rowSet[r][num] = struct{}{}
			colSet[c][num] = struct{}{}
			boxSet[boxIndexInOneDimension][num] = struct{}{}
		}
	}

	return result
}
