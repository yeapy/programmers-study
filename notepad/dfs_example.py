graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3]
]

visited = [False] * len(graph)
stack = [1]

while stack:
    node = stack.pop()

    if visited[node]:
        continue

    visited[node] = True
    print(node)

    for next_node in reversed(graph[node]):
        if not visited[next_node]:
            stack.append(next_node)