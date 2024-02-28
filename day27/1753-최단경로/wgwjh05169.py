import sys


def get_input():
    input = sys.stdin.readline

    v, e = map(int, input().split(' '))
    k = int(input())
    edges = []
    for _ in range(e):
        edges.append(list(map(int, input().split(' '))))

    return v, e, k, edges


inf = float('inf')
def solution(V, E, k, edges):
    adj_list = [[] for _ in range(V)]
    for u, v, w in edges:
        u -= 1
        v -= 1
        adj_list[u].append((v, w))

    dist_to = dijkstra(adj_list, k-1, V)
    print(*dist_to, sep='\n')


def dijkstra(adj_list, k, V):
    dist_to = []
    for i in range(V):
        dist_to.append(get_dist(adj_list, k, i))

    minimum = inf
    mi = None
    for i in range(V):
        if dist_to[i] < minimum:
            minimum = dist_to[i]
            mi = i

    for _ in range(V):
        flag = True
        for j in range(V):
            d = dist_to[mi] + get_dist(adj_list, mi, j)
            if d < dist_to[j]:
                dist_to[j] = d
                flag = False

            if dist_to[j] < minimum:
                minimum = dist_to[j]
                mi = j

        if flag:
            break

    dist_to[k] = 0

    return dist_to


def get_dist(adj_list, u, v):
    for vertax in adj_list[u]:
        if vertax[0] == v:
            return vertax[1]

    return inf


solution(*get_input())


# 8:43 메모리초과
# 8:49 인접리스트로 수정 - 시간초과
# 8:54 find_min()을 dist_to update 과정과 합침 - 2% 시간초과
# 9:02 dist_to 업데이트 후 변화가 없으면 break - 2% 틀
