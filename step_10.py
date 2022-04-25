import sys
#2798 https://www.acmicpc.net/problem/2798
N,M=map(int,sys.stdin.readline().split())

a=list(map(int,sys.stdin.readline().split()))
a.reverse()
result=0

for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k] > M:
                continue
            else:
                result=max(result,a[i]+a[j]+a[k])

print(result)


#2231 https://www.acmicpc.net/problem/2231

N=int(sys.stdin.readline().rstrip())
#print(N)

for i in range(1,N+1):
    num = list(map(int,str(i)))
    num_sum=i+sum(num)
    if num_sum==N:
        print(i)
        break
    if i==N:
        print(0)


#7568 https://www.acmicpc.net/problem/7568

N=int(sys.stdin.readline().rstrip())
stu_list=[]

for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    stu_list.append((x,y))
    print(stu_list)

for j in stu_list:
    rank=1
    for k in stu_list:
        if(j[0]!=k[0]) & (j[1]!=k[1]):
            if(j[0]<k[0]) & (j[1]<k[1]):
                rank+=1
    print(rank,end=" ")


#1436 https://www.acmicpc.net/problem/1436

N=int(sys.stdin.readline().rstrip())
a=666
cnt=0

while True:
    if '666' in str(a):
        cnt+=1
    if cnt == N:
        print(a)
        break
    a+=1

