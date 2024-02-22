from collections import deque
import copy


def get_input():
    fishes = []
    for _ in range(4):
        fishes.append(list(map(int, input().split(" "))))

    return fishes


direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]          # [상어, 1~16 물고기]의 방향
def solve(fish_list):
    matrix, fishes, ans = init(fish_list)

    ans = bfs(matrix, fishes, ans)
    print(ans)

def init(fish_list):
    matrix = [[None] * 4 for _ in range(4)]
    fishes = [None] * 17

    # 어항 세팅
    for i in range(4):
        for j in range(0, 8, 2):
            idx = fish_list[i][j]
            matrix[i][j // 2] = (idx, fish_list[i][j+1] - 1)
            fishes[idx] = (i, j // 2)

    # 상어 세팅
    t = eat(matrix, fishes, 0, 0)

    # 물고기 이동
    move(matrix, fishes)

    return matrix, fishes, t


def eat(matrix, fishes, i, j):
    shark = fishes[0]
    if shark:
        si, sj = shark
        matrix[si][sj] = (-1, -1)

    target = matrix[i][j]
    matrix[i][j] = (0, target[1])
    fishes[0] = (i, j)
    fishes[target[0]] = None

    return target[0]


def move(matrix, fishes):
    for fi in range(1, 17):
        if not fishes[fi]:
            continue

        next = find_next(matrix, fishes, fi)
        if not next:
            return

        i, j = fishes[fi]
        mine = matrix[i][j]

        ti, tj = next
        target = matrix[ti][tj]

        matrix[i][j], matrix[ti][tj] = matrix[ti][tj], matrix[i][j]
        fishes[mine[0]] = (ti, tj)
        if target != (-1, -1):
            fishes[target[0]] = i, j

    return


def find_next(matrix, fishes, fi):
    i, j = fishes[fi]
    idx, d = matrix[i][j]
    di, dj = direction[d]
    for _ in range(9):
        if can_go(matrix, i + di, j + dj):
            matrix[i][j] = (idx, d)
            return i + di, j + dj

        d = (d + 1) % 8
        di, dj = direction[d]

    return None


def can_go(matrix, i, j):
    if not (0 <= i < 4 and 0 <= j < 4):
        return False

    if matrix[i][j][0] == 0:
        return False

    return True


def bfs(m, f, a):
    maximum = 0
    queue = deque()
    queue.append((m, f, a))

    while queue:
        origin_matrix, origin_fishes, ans = queue.popleft()

        si, sj = origin_fishes[0]
        di, dj = direction[origin_matrix[si][sj][1]]
        prev = len(queue)
        for k in range(1, 5):
            new_i, new_j = si + di * k, sj + dj * k
            if 0 <= new_i < 4 and 0 <= new_j < 4 and origin_matrix[new_i][new_j] != (-1, -1):
                new_matrix = copy.deepcopy(origin_matrix)
                new_fishes = origin_fishes[:]

                res = eat(new_matrix, new_fishes, new_i, new_j)
                move(new_matrix, new_fishes)

                queue.append((new_matrix, new_fishes, ans + res))

        if len(queue) == prev:
            maximum = max(ans, maximum)

    return maximum


solve(get_input())
