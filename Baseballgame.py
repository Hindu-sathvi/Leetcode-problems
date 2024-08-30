#https://leetcode.com/problems/baseball-game/description/
#code:
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        
        for op in operations:
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))
        
        return sum(record)
solution = Solution()
ops1 = ["5","2","C","D","+"]
ops2 = ["5","-2","4","C","D","9","+","+"]
ops3 = ["1","C"]

print(solution.calPoints(ops1))
print(solution.calPoints(ops2))  
print(solution.calPoints(ops3))  
