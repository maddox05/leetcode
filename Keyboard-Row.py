row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

rowMap = {
}
for i in row1:
    rowMap[i] = 1

for i in row2:
    rowMap[i] = 2
for i in row3:
    rowMap[i] = 3

def keyboard_row(words):
    words_y_switches= []
    maxSwitches= -68
    
    for i in words:
        pastRowNumb = None
        switches=0
        for j in i:
            j=j.lower()
            if(pastRowNumb!= None and pastRowNumb != rowMap.get(j)):
                switches+=1
            pastRowNumb=rowMap.get(j)
        if(switches> maxSwitches):
            maxSwitches=switches
        words_y_switches.append((switches,i))
    ret = []
    for i in words_y_switches:
        if(i[0]==0):
            ret.append(i[1])
    return ret

        




class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return keyboard_row(words)
        
