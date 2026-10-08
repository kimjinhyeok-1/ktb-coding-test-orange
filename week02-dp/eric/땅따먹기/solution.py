def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][2], land[i - 1][1])

    return max(land[len(land) - 1])

# def solution(land):
#     result = 0
#     pre_cul = -1

#     for i in range(len(land)):
#         cul, num = nextrow(land[i], pre_cul)

#         pre_cul = cul
#         result += num

#     return result

# def nextrow(arr, k):
#     max = 0
#     idx = 0

#     for i in range(4):
#         if i == k:
#             continue

#         if arr[i] > max:
#             max = arr[i]
#             idx = i

#     return idx, max

# 배열과 이전 인덱스를 주면 나머지 중 최댓값 찾는 함수.
#
