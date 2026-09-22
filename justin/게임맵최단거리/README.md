# 문제 설명
벽이 존재하는좌표 (1,1)에서 좌표 (5,5)에 도착하는 최단거리

# 문제 접근
최단거리 탐색은 주로 BFS를 활용함.
DFS로도 최단거리 탐색을 풀 수 있지만, 이동 횟수(재귀 depth)를 매번 전달하며 최단 거리를 갱신해줘야함.

1. 현재 위치를 큐에 넣는다.
2. 현재 위치를 큐에서 뺀다.
3. 방문할 수 있는 모든 위치를 큐에 넣는다.
4. 상대 진영인 (n, m)에 도착할 때까지 반복한다.
5. 방문할 수 있는 위치는 '1'이다.

2차원 배열에서 상하좌우가 헷갈려서 먼저 현재 위치에서 방문할 수 있는 위치를 계산하는 코드를 짰다.


from collections import deque
def solution(maps):
    queue = deque()
    queue.append((0,0))
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    n = len(maps)
    m = len(maps[0])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx,ny))
                print(queue)
            
    return

# 소요 시간 40분
visited(distance) 배열을 생각을 못했다.
더 최적화 하는 방법으로는 maps배열안에 저장을해도되고, maps를 원본으로 보존해야 한다면 visited 배열을 사용하는 방법이 있겠다