#1712 https://www.acmicpc.net/problem/1712 다시
import sys
A,B,C = map(int,sys.stdin.readline().split())
'''
A=고정비용
B=가변비용(인건비, 재료비)
C=노트북 가격, 개수 = n

C*n >= A+(B*n)가 되려면
C가 몇이여야 하나?

n >= (A+B)/C
cnt=0
for n in range(1000000000):
    if n <= A/(C-B):
        cnt+=1

if cnt >0:
    print(cnt)
else:
    print(-1)
이렇게 하니까 시간초과

n = A/(C-B) 이렇게 하면 런타임 에러
'''

if B >= C:
    print(-1)
else:
    print(int(A/(C-B))+1)

#2292 https://www.acmicpc.net/problem/2292 다시
import sys
'''
2~7: 
8~19:
20~37:
38~61:
규칙을 모르겠음
6의 배수
'''

n=int(sys.stdin.readline().rstrip())
tile=1
cnt=0

while n > tile:
    tile += 6 * cnt
    cnt+=1
print(cnt)


#1193 https://www.acmicpc.net/problem/1193 다시 
import sys
n=int(sys.stdin.readline().rstrip())
line=1

while n > line:
    n-=line
    line+=1

if line%2 ==0:
    num1=n
    num2=line-n+1
else:
    num1=line-n+1
    num2=n
print(num1,'/',num2,sep="")


#2869 https://www.acmicpc.net/problem/2869 다시
import sys
import math
A,B,V=map(int,sys.stdin.readline().split())

'''
day = (V-B)/(A-B)
math.ceil ==> 올림
math.floor ==> 내림

'''
day = (V-B)/(A-B)
print(math.ceil(day))

#10250 https://www.acmicpc.net/problem/10250 
import sys

T=int(sys.stdin.readline().rstrip())
for i in range(T):
    H,W,N=map(int,sys.stdin.readline().split())
    #H=층수, W=각층의 방수, N=몇번째 손님
    #6 12 10 = 402
    A=(N%H)
    B=(N//H)+1
    if A==0:
        #print(H,B-1,sep="0")
        print(H*100+(B-1))
    else:
        #print(A,B,sep="0")
        print(A*100+B)

        
#2775 https://www.acmicpc.net/problem/2775 다시 
import sys

T=int(sys.stdin.readline().rstrip())
for i in range(T):
    k=int(sys.stdin.readline().rstrip())#1층
    n=int(sys.stdin.readline().rstrip())#3호

    val = [val for val in range(1,n+1)]
    #print(val)

    for j in range(k):
        for k in range(1,n):
            val[k] += val[k-1]
            #print(val)
    print(val[-1])

    
#2839 https://www.acmicpc.net/problem/2839 다시 
import sys

N=int(sys.stdin.readline().rstrip()) #N키로
#3,5키로로 나눠서
#18 ==> 5*3 + 3*1 ==> 4개
'''
a=N//5
N=N-(5*a)
b=N//3
a+b'''
box=0
while True:
    if N%5==0:
        box=box+(N//5)
        print(box)
        break
    #print("N:",N)
    N=N-3
    #print("N:",N)
    #print("box",box)
    box+=1
    if N<0:
        print(-1)
        break

#10757 https://www.acmicpc.net/problem/10757 
import sys

A,B=map(int,sys.stdin.readline().split())
print(A+B)


