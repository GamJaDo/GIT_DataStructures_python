def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)

        nbr = graph[vertex] - visited
        for v in nbr:
            dfs_cc(graph, color, v, visited)

    return color

def find_connected_component(graph):
    visited = set()
    colorList = []

    for vtx in graph:
        if vtx not in visited:
            color = dfs_cc(graph, [], vtx, visited)
            colorList.append(color)

    print("그래프 연결성분 개수 = %d" %len(colorList))
    print(colorList)


graph = {"A" : set(["B", "C"]),
         "B" : set(["A"]),
         "C" : set(["A"]),
         "D" : set(["E"]),
         "E" : set(["D"]),
         }

print("find_connected_component: ")
find_connected_component(graph)
