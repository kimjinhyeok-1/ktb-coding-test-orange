# [타겟 넘버]
# 접근법:
# - 각 숫자마다 + / - 두 가지 선택지가 존재
# - 모든 경우를 확인해야 하므로 DFS 사용
# - 상태는 현재 index, 현재까지의 합
#
# 생각해야 되는 것:
# - 매 단계 선택지가 몇 개인가?
# - 모든 경우를 탐색해야 하는가?
# - 종료 조건은 언제인가?
# - 재귀에 어떤 값을 넘겨야 하는가?
#
# 시간복잡도:
# - 각 숫자마다 2개의 선택지
# - 총 경우의 수는 2^N
# - O(2^N)

def solution(numbers, target):
    n = len(numbers)
    def dfs(cnt, val):
        if cnt == n:
            if val == target:
                return 1
            else:
                return 0
        else:
            answer = 0
            answer += dfs(cnt+1, val+numbers[cnt])
            answer += dfs(cnt+1, val-numbers[cnt])
        return answer
    
    answer = dfs(0, 0)
    return answer