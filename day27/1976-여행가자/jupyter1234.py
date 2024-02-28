import sys
#E C B C D 이 주어지면 E-A-B-C-B-C-B-D 이렇게 탐색함
def main():
    n = int(input())
    m = int(input())
    parent = [0] * (n+1)
    # for _ in range(n):

    #1부터 N
    mat = [[0] * (n+1)]
    temp = []
    for _ in range(n):
        line = sys.stdin.readline().split()
        temp.append(line)
    #순서대로 방문해야하는 도시
    city = sys.stdin.readline().split() 

    #1부터 시작하게
    for t in temp:
        arr = [0]
        for i in t:
            arr.append(int(i))
        mat.append(arr)
    # print(mat)
        
    #부모 초기화
    for i in range(1,n+1):
        parent[i] = i
    # print(parent)

    #union 노드 연결
    for i in range(1,n+1):
        for j in range(1,n+1):
            if mat[i][j] == 1:   #연결됨
                #union
                union(i,j,parent)
    # print(parent)
    group = parent[int(city[0])]
    if check(parent,city,group):
        print("YES")
    else:
        print("NO")
    

def check(parent,city,group):
    for c in city:
        if parent[int(c)] != group:
            return False
    return True



def union(i,j,parent):
    #각자 노드의 부모 찾고 큰놈을 작은놈으로 연결
    i = find(i,parent)
    j = find(j,parent)
    if i < j : 
        parent[j] = i
    else:
        parent[i] = j


def find(u,parent):
    if parent[u] != u:  
        parent[u] = find(parent[u],parent)  #계속 거슬러 올라가기
    return parent[u]

main() 
