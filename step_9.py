#10872 https://www.acmicpc.net/problem/10872  
import sys

N=int(sys.stdin.readline().rstrip())

def fac(n):
    res=1
    if n>0:
        return n*fac(n-1)
    if n==0:
        return 1


print(fac(N))

#10870 https://www.acmicpc.net/problem/10870
import sys

N=int(sys.stdin.readline().rstrip())

def p(n):
    sum=0
    if n<=1:
        return n
    elif n>=2:
        return p(n-1)+p(n-2)
    

#2447 https://www.acmicpc.net/problem/2447 다시
import sys

N=int(sys.stdin.readline().rstrip())

def star(n):
    if n==3:
        return ['***',"* *","***"]
    arr=star(n//3)
    stars=[]

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(N)))

#2447 https://www.acmicpc.net/problem/2447 다시
import sys

N=int(sys.stdin.readline().rstrip())

def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end)
    print(start,end)
    hanoi(n-1,6-start-end,end)

print(2**N-1)
hanoi(N,1,3)

    

print(p(N))

