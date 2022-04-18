import sys
#1978 https://www.acmicpc.net/problem/1978 다시

N=int(sys.stdin.readline().rstrip())
a=list(map(int,sys.stdin.readline().split()))

sosu=0

for i in a:
    cnt=0
    if i==1:
        continue
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
            #print(i,j,i%j,cnt)
    #print(cnt)
    if(cnt == 1):
        sosu+=1
print(sosu)


#2581 https://www.acmicpc.net/problem/2581
M=int(sys.stdin.readline().rstrip())
N=int(sys.stdin.readline().rstrip())
b=[]

for i in range(M,N+1):
    cnt=0
    for j in range(2,i+1):
        if i==1:
            continue
        elif i%j == 0:
            cnt+=1
            if cnt>2:
                break
    if cnt==1:
        b.append(i)
    
if len(b)>0:
    print(sum(b))
    print(b[0])
else:
    print(-1)


#11653 https://www.acmicpc.net/problem/11653 다시 
N=int(sys.stdin.readline().rstrip())
if N==1:
    print('')

for i in range(2,N+1):
    if N%i==0:
        while N%i==0:
            print(i)
            N=N/i

#1929 https://www.acmicpc.net/problem/1929
def sosu(start,end):
    b=[]
    for i in range(start,end+1):
        count=0
        for j in range(2,i+1):
            if i==1:
                continue
            elif i%j==0:
                count+=1
                if count>2:
                    break
        if count==1:
            #b.append(i)
            print(i)
    return b        


M,N=map(int,sys.stdin.readline().split())
result=sosu(M,N)


#1929 https://www.acmicpc.net/problem/1929 너무 어려워...
m,n=map(int,sys.stdin.readline().split())

prime_list = [True] * (n+1)
x=int((n+1)**0.5)
for i in range(2,x+1):
    if prime_list[i] == True:
        for j in range(i+i, n+1, i):
            prime_list[j]=False

sieve = []
for i in range(2,n+1):
    if prime_list[i] == True:
        sieve.append(i)

for i in range(len(sieve)):
    if sieve[i] >= m:
        print(sieve[i])
