#https://leetcode.com/problems/find-center-of-star-graph/?envType=problem-list-v2&envId=graph
#code:
class Solution(object):
    def findCenter(self,edges):
        count = {}

        for u, v in edges:
            if u in count:
                count[u] += 1
            else:
                count[u] = 1
        
            if v in count:
                count[v] += 1
            else:
                count[v] = 1
  
        for node, counts in count.items():
            if counts == len(edges):  
                return node
solution=Solution()
edges1 = [[1, 2], [2, 3], [4, 2]]
print(solution.findCenter(edges1)) 
