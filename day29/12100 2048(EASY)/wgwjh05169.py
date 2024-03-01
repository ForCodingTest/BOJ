# 7:47~8:22

import copy
import sys
from collections import deque


input = sys.stdin.readline


def get_input():
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split(' '))))

    return N, board


def solution(N, board):
    return max(bfs(N, board))


def bfs(N, board):
    queue = deque()
    queue.append((copy.deepcopy(board), 0))

    result = []
    while queue:
        b, depth = queue.popleft()
        if depth == 5:
            m = -1
            for i in range(N):
                m = max(m, max(b[i]))
            result.append(m)
            continue

        queue.append((move(N, copy.deepcopy(b)), depth + 1))
        b = list(map(lambda x: list(reversed(x)), list(zip(*b))))
        queue.append((move(N, copy.deepcopy(b)), depth + 1))
        b = list(map(lambda x: list(reversed(x)), list(zip(*b))))
        queue.append((move(N, copy.deepcopy(b)), depth + 1))
        b = list(map(lambda x: list(reversed(x)), list(zip(*b))))
        queue.append((move(N, copy.deepcopy(b)), depth + 1))

    return result


def move(N, board):
    for i in range(N):
        prev = False
        for j in range(1, N):
            if board[i][j] != 0:
                prev = go(N, board, i, j, prev)

    return board


def go(N, board, i, j, prev):
    tj = j - 1
    while 0 <= tj < N:
        if board[i][tj] == 0:
            if tj == 0:
                board[i][tj] = board[i][j]
                board[i][j] = 0
                return False
            else:
                tj -= 1
        else:
            if board[i][tj] == board[i][j] and not prev:
                board[i][tj] *= 2
                board[i][j] = 0
                return True
            else:
                if tj != j - 1:
                    tj += 1
                    board[i][tj], board[i][j] = board[i][j], board[i][tj]
                return False

    return False


print(solution(*get_input()))
