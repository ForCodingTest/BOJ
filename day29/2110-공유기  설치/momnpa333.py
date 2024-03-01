import sys
input=sys.stdin.readline

N,C=map(int,input().split(' '))

wifi=sorted([int(input()) for i in range(N)])
answer=[]
# print(wifi)

def isposi(dist,C):
    prev=wifi[0]
    for item in wifi[1:]:
        if item-prev>=dist:
            prev=item
            C-=1
        if C==1:
            answer.append(dist)
            return True
    return False

def bisearch(start,end,C):
    if start>end:
        return False
    mid=(start+end)//2

    if isposi(mid,C):
        bisearch(mid+1,end,C)
    else:
        bisearch(start,mid-1,C)
bisearch(0,1000000000,C)
print(max(answer))

#7:58