def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            for t in graph[n]:
                stack.append(t)

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

print(dfs(graph, "A"))
