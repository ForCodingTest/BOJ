import sys
input = sys.stdin.readline


def get_input():
    N, M = map(int, input().split(' '))
    bus = []
    for _ in range(M):
        bus.append(list(map(int, input().split(' '))))

    return N, M, bus


inf = float('INF')
def solution(N, M, bus):
    for i in range(M):
        bus[i][0] -= 1
        bus[i][1] -= 1

    result = bellman_ford(N, bus)
    if not result:
        print(-1)
        return

    for dist in result[1:]:
        if dist == inf:
            print(-1)
        else:
            print(dist)


def bellman_ford(N, bus):
    dist_to = [inf] * N
    dist_to[0] = 0

    # find shortest distance
    for _ in range(N):
        for u, v, w in bus:
            if dist_to[u] + w < dist_to[v]:
                dist_to[v] = dist_to[u] + w

    # check negative cycle
    for u, v, w in bus:
        if dist_to[u] + w < dist_to[v]:
            return False

    return dist_to


solution(*get_input())
