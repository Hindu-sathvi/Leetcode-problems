#https://leetcode.com/problems/pascals-triangle-ii/?envType=problem-list-v2&envId=array
#Code:
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        for i in range(1,rowIndex+1):
            row.append(1)
            for j in range(len(row)-2,0,-1):
                row[j]=row[j]+row[j-1]
        return row
