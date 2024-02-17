# 21:52~23:23

import sys
input = sys.stdin.readline


dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def get_input():
    N, M, K = map(int, input().split(' '))
    fireballs = []
    for _ in range(M):
        fireballs.append(input())

    return N, M, K, fireballs


def solve(N, M, K, fireballs):
    matrix, fireballs = set_fireball(N, M, fireballs)

    for _ in range(K):
        run(N, matrix, fireballs)

    sum_of_m = 0
    for fireball in fireballs.values():
        sum_of_m += fireball[0]

    return sum_of_m


def set_fireball(N, M, fireballs):
    global new_idx

    matrix = [[[] for j in range(N)] for i in range(N)]
    for i in range(M):
        r, c, m, s, d = map(int, fireballs[i].split(" "))
        r -= 1
        c -= 1

        fireballs[i] = [m, s, d]
        matrix[r][c].append(i)

    fireballs = {i: fireball for i, fireball in enumerate(fireballs)}
    new_idx = M

    return matrix, fireballs


def run(N, matrix, fireballs):
    global visited

    # move
    visited = set()
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                target = []
                for k in range(len(matrix[i][j])):
                    idx = matrix[i][j][k]
                    if idx not in visited:
                        target.append(idx)
                        move(N, matrix, i, j, idx, fireballs)

                for t in target:
                    matrix[i][j].remove(t)

    # combine & divide
    for i in range(N):
        for j in range(N):
            if matrix[i][j] and len(matrix[i][j]) > 1:
                combine_and_divide(matrix, i, j, fireballs)


def move(N, matrix, i, j, idx, fireballs):
    global visited

    visited.add(idx)

    m, s, d = fireballs[idx]
    d = dirs[d]
    new_i = (i + (d[0] * s) + N * 1000) % N
    new_j = (j + (d[1] * s) + N * 1000) % N

    matrix[new_i][new_j].append(idx)


def combine_and_divide(matrix, i, j, fireballs):
    global new_idx

    sum_of_m = 0
    sum_of_s = 0
    is_even = True
    is_odd = True
    for idx in matrix[i][j]:
        m, s, d = fireballs.pop(idx)
        sum_of_m += m
        sum_of_s += s
        if d % 2 == 0 and is_odd:
            is_odd = False
        if d % 2 == 1 and is_even:
            is_even = False

    new_m = int(sum_of_m / 5)
    new_s = int(sum_of_s / len(matrix[i][j]))
    if is_odd or is_even:
        new_d = [0, 2, 4, 6]
    else:
        new_d = [1, 3, 5, 7]

    matrix[i][j].clear()
    if new_m == 0:
        return

    for di in range(4):
        matrix[i][j].append(new_idx)
        fireballs[new_idx] = [new_m, new_s, new_d[di]]
        new_idx += 1


print(solve(*get_input()))
