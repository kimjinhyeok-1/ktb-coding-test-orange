def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(v):
        visited[v] = True

        for next_node in range(n):
            if computers[v][next_node] == 1 and not visited[next_node]:
                dfs(next_node)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer


# 1. 이어진 덩어리를 찾는 문제이므로 DFS를 적용한다.
# 2. visited는 컴퓨터별 방문 여부를 저장한다.
# 3. DFS는 한 덩어리를 전부 방문 처리한다.
# 4. 전체 컴퓨터를 순회하다 미방문 컴퓨터를 만나면 새로운 덩어리이므로 answer를 1 늘리고 DFS를 시작한다.
# 5. 인접 행렬에서는 현재 행 전체를 보며 연결된 노드를 찾는다.
