import sys


def get_input():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    cities = []
    for _ in range(n):
        cities.append(list(map(int, input().split(' '))))
    plan = list(map(int, input().split(' ')))

    return n, m, cities, plan


def solution(n, m, cities, plan):
    global parent

    plan = list(map(lambda x: x-1, plan))

    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if cities[i][j] == 1:
                union(i, j)

    for i in range(m - 1):
        if find(plan[i]) != find(plan[i + 1]):
            print("NO")
            return
    print("YES")


def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(x, y):
    parent[find(x)] = parent[find(y)]


solution(*get_input())
