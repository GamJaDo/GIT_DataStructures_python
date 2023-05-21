def dfs(graph, start, visited):
    visited.append(start)

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

graph = { "A" : ["B", "C"],
          "B" : ["A", "D"],
          "C" : ["A", "D", "E"],
          "D" : ["B", "C", "F"],
          "E" : ["C", "G", "H"],
          "F" : ["D"],
          "G" : ["E", "H"],
          "H" : ["E", "G"],
          }

visited = []
dfs(graph, "A", visited)
print(visited)
