class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []
        for i in range(1, numRows+1):
            row = [0]*i
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(row)
        
        return ans
