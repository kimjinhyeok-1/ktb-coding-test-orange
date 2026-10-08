# import math

def solution(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567


# def solution(n):
#     if n == 1 :
#         return 1

#     elif n == 2 :
#         return 2

#     else:
#         answer = 1
#         two = 0

#         for i in range(n // 2):
#             n -= 2
#             two += 1
#             if n > 0 :
#                 answer += math.factorial(n+1+i) // (math.factorial(two) * math.factorial(n))
#             if n == 0:
#                 answer += 1

#     return answer % 1234567


"""
보자마자 DP 접근은 생각 못했습니다.
문제 설명에 나와있는 숫자를 보고 조합이 떠올라서 한 번 생각이 글로 빠지니까 다른 방향으로 전환이 어려운 것 같습니다.
시간 복잡도는 O(n^2)으로 DP : O(n)보다 오래걸려서 시간복잡도를 고려해야 되는 문제였으면 틀렸을 것 같습니다.
"""