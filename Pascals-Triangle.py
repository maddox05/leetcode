def gen_pascals_triangle(n):
    rows = []
    for i in range(0,n): # creation of rows
        rows.append([])
        for j in range(0,i+1): # creation of innerds of rows (cols kinda)
            if(j==0 or j==i):
                 rows[i].append(1)
            else:
                rows[i].append(rows[i-1][j-1]+rows[i-1][j])
    return rows

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return gen_pascals_triangle(numRows)
