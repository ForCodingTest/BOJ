import sys
import heapq


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
    adj_list = [dict() for _ in range(V)]
    for u, v, w in edges:
        u -= 1
        v -= 1
        if adj_list[u].get(v):
            if w < adj_list[u][v]:
                adj_list[u][v] = w
        else:
            adj_list[u][v] = w

    dist_to = map(lambda x: 'INF' if x == inf else x, dijkstra(adj_list, k-1, V))
    print(*dist_to, sep='\n')


def dijkstra(adj_list, k, V):
    heap = []
    dist_to = [inf] * V
    for v in range(V):
        if v == k:
            dist_to[k] = 0
            heapq.heappush(heap, (0, k))
        elif adj_list[k].get(v):
            dist_to[v] = adj_list[k][v]
            heapq.heappush(heap, (adj_list[k][v], v))

    while heap:
        _, u = heapq.heappop(heap)
        for v in adj_list[u].keys():
            new_dist = dist_to[u] + adj_list[u][v]
            if new_dist < dist_to[v]:
                dist_to[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist_to


solution(*get_input())
