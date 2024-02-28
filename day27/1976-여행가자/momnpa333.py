v=int(input())
M=int(input())


parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 특정 원소가 속한 집합을 찾기
def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

   
# 두 원소가 속한 집합을 합치기
def union(a, b):
    a=find(a)
    b=find(b)

    if a<b:
        parent[b]=parent[a]
    else:
        parent[a]=parent[b]

    
for i in range(1, v + 1):
    parent[i] = i

for i in range(1,v+1):
    for j,v in enumerate(map(int,input().split(' '))):
        if v==1:
            union(i,j+1)
            # print(parent)


findary=list(map(int,input().split(' ')))

tmp=set()
for i in findary:
    tmp.add(find(i))
    print(find(i))

if len(tmp)==1:
    print("YES")
else:
    print("NO")
