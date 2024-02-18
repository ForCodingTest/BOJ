# 18:40~
# 19:35~ 구현 다 됐는데 일부 테케가 이상하게 나옴.. 왜지..
# 19:39 0퍼틀 아니 시발 왜???
# 19:44 덩어리가 없으면 0 반환 ㅎㅎ. 근데 고쳐도 똑같애
# 20:03 get_cnt에서 완탐이 아니라 이중포문 완탐으로 했는데, 오른쪽으로만 내려가서 왼쪽으로 연결된 테케가 안 됨
# 20:20 solve


import sys
from collections import deque
input = sys.stdin.readline


def get_input():
    N, Q = map(int, input().split(" "))
    matrix = []
    for _ in range(2 ** N):
        matrix.append(list(map(int, input().split())))

    L = list(map(int, input().split(" ")))

    return N, Q, matrix, L


near = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def solve(N, Q, matrix, L):
    n = 2 ** N
    for level in L:
        l = 2 ** level
        if l != 1:
            divide_and_rotate(matrix, n, l)
            # print(l, end=' ')
            # print('회전 후', *matrix, sep='\n')
        check(matrix, n)
        # print('체크 후', *matrix, sep='\n')

    print(get_sum(matrix, n))
    print(get_cnt(matrix, n))


def divide_and_rotate(matrix, n, l):
    for i in range(0, n, l):
        for j in range(0, n, l):
            rotate(matrix, i, j, l)


def rotate(matrix, i, j, l):
    temp = []
    for di in range(l):
        temp.append(matrix[i + di][j:j+l])
    new = list(map(lambda x: list(reversed(list(x))), zip(*temp)))

    for di in range(l):
        for dj in range(l):
            matrix[i + di][j + dj] = new[di][dj]


def check(matrix, n):
    target = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                cnt = 0
                for di, dj in near:
                    if 0 <= i + di < n and 0 <= j + dj < n:
                        if matrix[i+di][j+dj] > 0:
                            cnt += 1

                if cnt < 3:
                    target.append((i, j))

    for i, j in target:
        matrix[i][j] -= 1


def get_sum(matrix, n):
    sum_of_ice = 0
    for i in range(n):
        sum_of_ice += sum(matrix[i])

    return sum_of_ice


def get_cnt(matrix, n):
    global visited

    maximum = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] and not visited[i][j]:
                result = bfs(matrix, n, i, j)
                if result > maximum:
                    maximum = result

    return maximum
    # sets = []
    # for i in range(n):
    #     for j in range(n):
    #         if matrix[i][j] <= 0:
    #             continue
    #
    #         num = i * n + j
    #         if not sets:
    #             sets.append(set())
    #             sets[-1].add(num)
    #
    #         idx = -1
    #         for si in range(len(sets)):
    #             if num in sets[si]:
    #                 idx = si
    #                 break
    #         if idx == -1:
    #             idx = len(sets)
    #             sets.append(set())
    #             sets[idx].add(num)
    #
    #         for di, dj in near:
    #             if 0 <= i + di < n and 0 <= j + dj < n:
    #                 if matrix[i + di][j + dj] > 0:
    #                     sets[idx].add((i + di) * n + j + dj)
    #
    # if len(sets) == 0:
    #     return 0
    #
    # return max(map(len, sets))


def bfs(matrix, n, si, sj):
    global visited

    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = True
    cnt = 0
    while queue:
        i, j = queue.popleft()
        cnt += 1

        for di, dj in near:
            if 0 <= i + di < n and 0 <= j + dj < n:
                if matrix[i+di][j+dj] and not visited[i + di][j + dj]:
                    queue.append((i + di, j + dj))
                    visited[i+di][j+dj] = True

    return cnt


solve(*get_input())
