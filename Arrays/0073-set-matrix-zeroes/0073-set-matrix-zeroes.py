'''
    Hint : in this approach we are using additional space to store rows
        and cols, where matrix[r][c]==0
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n, m = len(matrix), len(matrix[0])

        # using space
        rows, cols = set(), set()

        # checking for zeroes in matrix:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Setting zeroes:
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0

