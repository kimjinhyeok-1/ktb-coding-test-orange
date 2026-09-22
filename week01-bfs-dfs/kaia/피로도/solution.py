from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for order in permutations(dungeons):
        energy = k
        count = 0

        for required, cost in order:
            if energy < required:
                break

            energy -= cost
            count += 1

        answer = max(answer, count)

    return answer


