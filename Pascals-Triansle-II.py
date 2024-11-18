def gen_pascals_triangle(n):
    rows = []
    for i in range(0,n): # creation of rows
        rows=[]
        for j in range(0,i+1): # creation of innerds of rows (cols kinda)
            if(j==0 or j==i):
                 rows.append(1)
            else:
                rows.append(past_row[j-1]+past_row[j])

        past_row = rows
    return rows

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return gen_pascals_triangle(rowIndex+1)
