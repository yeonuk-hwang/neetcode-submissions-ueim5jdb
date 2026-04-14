class Solution:


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # convert 2D index to 1D

        row_count = len(matrix)
        column_count = len(matrix[0])
        width = column_count

        def convert_2d_to_1d_index(x:int, y:int) -> int:
            return x * width + y
        
        def convert_1d_to_2d(index:int) -> tuple[int, int]:
            return index // width, index % width

        left = 0
        right = convert_2d_to_1d_index(row_count - 1, column_count - 1)

        while left <= right:
            middle = left + ((right - left) // 2)

            x, y= convert_1d_to_2d(middle)
            middle_value = matrix[x][y]

            if middle_value == target:
                return True
            elif middle_value > target:
                right = middle - 1
            elif middle_value < target:
                left = middle + 1

        return False

