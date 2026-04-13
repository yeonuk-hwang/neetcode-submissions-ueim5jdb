class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterate each cell
        # find duplicate in each row, column, and small box
        # - find duplicate: using hash set
        # - how to represent all sets, columns, and small boxes using hash set?
        # using array
        # row = [set() * 9], column, small boxes

        row_sets = [set() for _ in range(9)]
        column_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                cell_value = board[row][column]
                if cell_value == ".":
                    continue

                if cell_value in row_sets[row]:
                    return False
                
                if cell_value in column_sets[column]:
                    return False
                
                current_box_row = row // 3
                current_box_column = column // 3
                boxes_per_row = 3
                current_box_index = current_box_row * boxes_per_row + current_box_column

                if cell_value in box_sets[current_box_index]:
                    return False

                row_sets[row].add(cell_value)
                column_sets[column].add(cell_value)
                box_sets[current_box_index].add(cell_value)

        return True

                



