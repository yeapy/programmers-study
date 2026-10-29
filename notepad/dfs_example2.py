numbers = [1, 2, 3]
visited = [False] * 3

def dfs(path):
    if len(path) == 2:
        print(path)
        return

    for i in range(3):
        if not visited[i]:
            visited[i] = True

            # ① 재귀 호출
            dfs(path + str(numbers[i]))
            # ② 방문 상태 복구
            visited[i] = False

dfs("")