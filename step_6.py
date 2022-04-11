#11654 https://www.acmicpc.net/problem/11654
import sys
n=sys.stdin.readline().rstrip()
print(ord(n))

'''
ord(): 문자의 아스키 코드값을 리턴하는 함수 (외우기)
chr(): 아스키 코드값 입력을 받아 그 코드에 해당하는 문자를 출력
'''

#11720 https://www.acmicpc.net/problem/11720
import sys
n=int(sys.stdin.readline().rstrip())

a=list(map(int,sys.stdin.readline().rstrip()))
print(sum(a))

#10809 https://www.acmicpc.net/problem/10809 다시
import sys
s=list(map(str,sys.stdin.readline().rstrip()))

alpha = list("abcdefghijklmnopqrstuvwxyz")


for i in alpha:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

#2675 https://www.acmicpc.net/problem/2675
import sys 
T=int(sys.stdin.readline().rstrip())


for i in range(T):
    n,S=list(map(str,sys.stdin.readline().split()))
    n=int(n)
    #print(S)
    for j in S:
        print(j*n,end="")
    print()

#1157 https://www.acmicpc.net/problem/1157 다시

import sys
S = sys.stdin.readline().rstrip().upper()
#print(S)
words = list(set(S))
#print(words)
cnt=[]

for i in words:
    count=S.count(i)
    cnt.append(count)
#print(cnt)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(words[cnt.index(max(cnt))])

#1152 https://www.acmicpc.net/problem/1152
import sys
S=list(map(str,sys.stdin.readline().split()))
print(len(S))

#2908 https://www.acmicpc.net/problem/2908 다시 
import sys
a,b=sys.stdin.readline().split()
#print(a,b)
a=int(a[::-1])
b=int(b[::-1])
#print(a,b)
if a<b:
    print(b)
else:
    print(a)


#5622 https://www.acmicpc.net/problem/5622 다시 
import sys

dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S = list(sys.stdin.readline().rstrip())
time=0

for i in S:
    for j in dial:
        if i in j:
            time+=dial.index(j) +3
print(time)


#2941 https://www.acmicpc.net/problem/2941 다시 
import sys
input=sys.stdin.readline().rstrip()
cro=["c=","c-","dz=","d-","lj","nj","s=","z="]
S=input

for i in cro:
    S=S.replace(i,'*')

print(len(S))


#1316 https://www.acmicpc.net/problem/1316 다시 
import sys
n=int(sys.stdin.readline().rstrip())
count=0

for i in range(n):
    w=sys.stdin.readline().rstrip()
    error=0
    for j in range(len(w)-1):
        if w[j] != w[j+1]:
            new_w=w[j+1:]
            if new_w.count(w[j]) > 0:
                error+=1
    if error ==0:
        count+=1
        
print(count)

