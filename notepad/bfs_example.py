from collections import deque

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3]
]

def bfs(start, n):
    # 직접 구현
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    result = []

    while queue:
        value = queue.popleft()
        result.append(value)
        
        for a in graph[value]:
            if visited[a] == False:
                visited[a] = True
                queue.append(a)

    return ' '.join(map(str,result))
    
    
print(bfs(1, 6))