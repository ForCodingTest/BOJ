# 11:19~12:32
# 11:50~12:20 예제 출력보다 더 많이 나와서 드랍... 잠깐 쉬자...
# 12:30 채점 시작

# 11:50에 틀렸던 건 38, 45 라인에서 -2 해야하는 걸 03 함 (per의 범위가 0-4인데 0-5로 착각)

import sys

input = sys.stdin.readline

direction = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
per = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, -1, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
for i in range(4):
    direction[i].append(per)
    per = per[:]
    per = list(reversed(list(zip(*per))))


def move(d, matrix, n):
    global i, j
    # 이동
    i += direction[d][0]
    j += direction[d][1]

    # 모래 흩날리기
    per = direction[d][2]   # 현재 방향에서의 흩날릴 비율
    present = matrix[i][j]  # y의 모래 양
    sum_of_out = [0, 0]     # y에서 나간 양, 격자 밖으로 나간 양
    ai, aj = None, None
    for pi in range(5):
        for pj in range(5):
            if per[pi][pj] == -1:
                ai, aj = pi, pj
                continue

            out = int(present * per[pi][pj])
            sum_of_out[0] += out
            di, dj = pi - 2, pj - 2
            if 0 <= i + di < n and 0 <= j + dj < n:
                matrix[i + di][j + dj] += out
            else:
                sum_of_out[1] += out

    reserved = present - sum_of_out[0]
    di, dj = ai - 2, aj - 2
    if 0 <= i + di < n and 0 <= j + dj < n:
        matrix[i + di][j + dj] += reserved
    else:
        sum_of_out[1] += reserved
    matrix[i][j] = 0

    return sum_of_out[1]


def solve(n, matrix):
    global i, j

    mid = n // 2
    length = 1
    d = 0
    i, j = mid, mid
    ans = 0
    while True:
        for _ in range(2):
            for k in range(length):
                ans += move(d, matrix, n)
                if i == 0 and j == 0:
                    return ans
            d = (d + 1) % 4
        length += 1


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(" "))))
print(solve(n, matrix))