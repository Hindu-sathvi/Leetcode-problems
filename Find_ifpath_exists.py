#https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=problem-list-v2&envId=graph
#Code:
from collections import deque
class Solution(object):
    def validPath(self,n, edges, source, destination):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v) 
            graph[v].append(u) 
        queue = deque([source])
        visited = [False] * n
        visited[source] = True  
        while queue:
            current_node = queue.popleft()
            if current_node == destination:
                return True
        
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True  
                    queue.append(neighbor)   
        return False

       

        
        