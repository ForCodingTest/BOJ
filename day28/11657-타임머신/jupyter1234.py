#도시의 개수 N
#간선 M
#가중치 0 가능 -> 벨만포드
#map으로 배열로 설정하고 다 도니깐 시간초과 -> defaultdict 사용
import sys
from collections import defaultdict
INF = float('inf')
n,m = map(int,input().split())
graphs = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())   #시작,도착,cost
    graphs[a-1].append([b-1,c])
dist = [INF] * n
dist[0] = 0
# print(graphs[0])
#벨만 시작
k = 0
negative = False
for k in range(n):
    for idx,value in graphs.items(): #조사 시작
            for nxt,c in value:
                if dist[idx] != INF and dist[idx] + c < dist[nxt]:
                    dist[nxt] = dist[idx] + c
                    if k == n-1:
                        negative = True
# print(dist)
if negative:
    print('-1')
else:
    for d in dist[1:]:
        if d == INF:
            print('-1')
        else:
            print(d)
#사이클이 있으면 -1, 없으면 dist 출력 (경로 없을 땐 -1)
