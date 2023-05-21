from collections import deque

def bfs(graph, start):
    visited = []
    q = deque([start])

    while q:
        n = q.popleft()
        
        if n not in visited:
            visited.append(n)
            
            for t in graph[n]:
                q.append(t)

    return visited

graph = { "A" : ["B", "C"],
          "B" : ["A", "D"],
          "C" : ["A", "D", "E"],
          "D" : ["B", "C", "F"],
          "E" : ["C", "G", "H"],
          "F" : ["D"],
          "G" : ["E", "H"],
          "H" : ["E", "G"],
          }

print(bfs(graph, "A"))
