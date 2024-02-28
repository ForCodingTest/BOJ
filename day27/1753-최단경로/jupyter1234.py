#방향그래프, 시작점에서 다른 모든 정점으로 향하는 최단 경로
import heapq
import sys
#v : 정점 e : 간선의 개수  1~v까지

def main():
    v,e  = map(int,input().split())
    k = int(input())  #시작정점

    dist = [98765432] * (v+1)  #초기 거리
    # visited =  [False] * (v+1)
    vert = {}
    #(u, v, w) 이는 u에서 v로 가는 가중치 w인 간선
    for _ in range(e):
        u,v,w = map(int,sys.stdin.readline().split())
        if u in vert:
            vert[u].append([v,w])
        else:
            vert[u] = [[v,w]]

    vert = dict(sorted(vert.items()))
    # print(vert)
    dist = dij(k,dist,vert)
    # print(dist)
    for i in range(1,len(dist)):
        if dist[i] == 98765432:
            print("INF")
        else:
            print(dist[i])


def dij(k,dist,vert):
    dist[k] = 0
    # visited[k] = True
    h = []
    heapq.heappush(h,(0,k))
    while h :
        c,k = heapq.heappop(h)
        if k in vert:
            for v,w in vert[k]:
                if c + w < dist[v]:
                    dist[v] = c + w
                    heapq.heappush(h,(c+w,v))
    return dist
main()
