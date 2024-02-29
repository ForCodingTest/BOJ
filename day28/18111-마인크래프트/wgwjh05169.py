# N*M 2차원 배열을 탐색하는 풀이 -> 30분 정도 풀고 시간초과 남
# dictionary 탐색 + pruning 으로 수정 -> 20분

import sys
from collections import defaultdict


input = sys.stdin.readline
def solution():
    N, M, B = map(int, input().split(' '))
    chunk = []

    maximum = 0
    minimum = 256
    blocks = defaultdict(int)
    for i in range(N):
        chunk.append(list(map(int, input().split(' '))))
        for j in range(M):
            blocks[chunk[i][j]] += 1
            if chunk[i][j] > maximum:
                maximum = chunk[i][j]
            if chunk[i][j] < minimum:
                minimum = chunk[i][j]

    ans = (256 * 500 * 500 * 2, None)
    for h in range(minimum, maximum + 1):
        result = get_fill(B, blocks, h, ans[0])
        if result:
            if result[0] < ans[0]:
                ans = result
            elif result[0] == ans[0] and result[1] > ans[1]:
                ans = result

    print(*ans)


def get_fill(B, blocks, height, present_ans):
    concave = 0
    convex = 0
    for block, cnt in blocks.items():
        if block > height:
            concave += (block - height) * cnt
        else:
            convex += (height - block) * cnt

        if concave * 2 + convex > present_ans:
            return None

    if concave + B >= convex:
        return concave * 2 + convex, height

    return None


solution()
