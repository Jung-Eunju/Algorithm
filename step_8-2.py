import sys

#2928 https://www.acmicpc.net/problem/4948
'''
def sosu(n):
    b=[]
    for i in range(n+1,2*n+1):
        cnt=0
        for j in range(2,i+1):
            if i==1:
                continue
            if i%j==0:
                cnt+=1
                if cnt>2:
                    break
        if cnt==1:
            b.append(i)
    return b
            
            

while True:
    N=int(sys.stdin.readline().rstrip())
    if N==0:
        break
    result = sosu(N)
    print(len(result))

'''
이렇게 하면 결과는 나오는데
속도가 너무 느리다...
'''

'''
def sosu(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

all_list=list(range(2,246912))
memo=[]

for i in all_list:
    if sosu(i):
        memo.append(i)

n=int(sys.stdin.readline().rstrip())

while True:
    count=0
    if n==0:
        break
    for i in memo:
        if n < i <= 2*n:
            count+=1
    print(count)
    n=int(sys.stdin.readline().rstrip())



#9020 https://www.acmicpc.net/problem/9020

check = [False, False] + [True] * 10000
for i in range(2, 101):
    if check[i] == True:
         for j in range(i + i, 10001, i):
              check[j] = False

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    n=int(sys.stdin.readline().rstrip())

    A=n//2
    B=A
    for j in range(int(n/2)):
        if check[A] and check[B]:
            print(A,B)
            break
        A-=1
        B+=1
        

    

#1085 https://www.acmicpc.net/problem/1085
x,y,w,h = map(int,sys.stdin.readline().split())

print(min(x,y,w-x,h-y))


#3009 https://www.acmicpc.net/problem/3009
x1,y1 = list(map(int,sys.stdin.readline().split()))
x2,y2 = list(map(int,sys.stdin.readline().split()))
x3,y3 = list(map(int,sys.stdin.readline().split()))

xlist=[x1,x2,x3]
ylist=[y1,y2,y3]

for i in range(3):
    if xlist.count(xlist[i])==1:
        x=xlist[i]
    if ylist.count(ylist[i])==1:
        y=ylist[i]

print(x,y)

#4153 https://www.acmicpc.net/problem/4153

'''
제곱 = a**2
'''

while True:
    a = list(map(int,sys.stdin.readline().split()))  
    if sum(a)==0:
        break
    a.sort()

    if (a[0]**2+a[1]**2) == a[2]**2:
        print("right")
    else:
        print("wrong")

import math
#3053 https://www.acmicpc.net/problem/3053

N=float(sys.stdin.readline().rstrip())

print("%6f" %(math.pi * N**2))
print("%6f" %(N*N*2))


#1002 https://www.acmicpc.net/problem/1002

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    d=((x2-x1)**2+(y2-y1)**2)**0.5

    rs = r1+r2
    rm=abs(r1-r2) #절대값

    if d==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if d==rs or d==rm:
            print(1)
        elif d<rs and d>rm:
            print(2)
        else:
            print(0)
    
