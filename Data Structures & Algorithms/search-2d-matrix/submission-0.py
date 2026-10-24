class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        curr_row, curr_col = rows-1, 0
        while (curr_row>=0 and curr_col<cols) :
            if matrix[curr_row][curr_col]==target :
                return True
            elif matrix[curr_row][curr_col]>target :
                curr_row-=1
            else :
                curr_col+=1
        
        return False