# [게임 맵 최단거리]
# 접근법:
# - 시작점에서 도착점까지 최소 이동 횟수를 구하는 문제
# - 모든 이동 비용이 동일하므로 BFS 사용
# - 상하좌우로 이동하며 방문하지 않은 좌표를 Queue에 추가
#
# 생각해야 되는 것:
# - 최단거리 문제인가?
# - 간선의 가중치가 모두 동일한가?
# - 방문 처리는 언제 해야 하는가?
# - 좌표의 범위를 벗어나지 않는지 확인해야 함
#
# 시간복잡도:
# - 각 칸을 최대 한 번 방문
# - N x M 크기의 맵
# - O(N * M)

from collections import deque
def solution(maps):
    q = deque([(0,0)])
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    r = len(maps)
    c = len(maps[0])
    dist = [[-1] * c for _ in range(r)]
    dist[0][0] = 1
    
    es = False
    while q:
        gr, gc = q.popleft()
        for dr, dc in d:
            nr, nc = gr + dr, gc + dc
            if nr == r-1 and nc == c-1:
                answer = dist[gr][gc] + 1
                return answer
            if 0<=nr<r and 0<=nc<c:
                if maps[nr][nc] == 1 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[gr][gc] + 1
                    q.append((nr,nc))
    
    answer = -1
    return answer
    

