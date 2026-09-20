# [단어 변환]
# 접근법:
# - 각 단어를 하나의 노드로 생각
# - 한 글자만 다른 단어끼리 이동 가능
# - 최소 변환 횟수를 구해야 하므로 BFS 사용
# - 현재 단어에서 변환 가능한 단어를 Queue에 추가
#
# 생각해야 되는 것:
# - 문자열 문제를 그래프로 볼 수 있는가?
# - 두 단어가 연결되는 조건은 무엇인가?
# - 이미 방문한 단어를 다시 볼 필요가 있는가?
# - target이 words에 없는 경우도 고려해야 함
#
# 시간복잡도:
# - 각 단어마다 다른 단어들을 비교
# - 단어 개수 N, 단어 길이 L
# - 단어 비교 비용까지 포함해 O(N^2 * L)

from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((0,begin))
    visited = {}
    if target not in words:
        return 0
    
    while q:
        cnt, word = q.popleft()
        
        if word == target:
            return cnt
        for next_word in words:
            temp = 0
            for i in range(len(next_word)):
                if word[i] != next_word[i]:
                    temp += 1
            if temp == 1 and next_word not in visited:
                visited[next_word] = True
                q.append((cnt + 1, next_word))
    return 0