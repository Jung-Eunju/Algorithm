
#10818
import sys
n=int(sys.stdin.readline().rstrip())

a=list(map(int,sys.stdin.readline().split()))
print(min(a),max(a),sep=' ')

#2562
import sys
n=[]

for i in range(9):
    n.append(int(sys.stdin.readline().rstrip()))

print(max(n))
print(n.index(max(n))+1)

'''
리스트 번호
리스트이름.index()
'''

#2577
import sys
a=[]
gop=1
for i in range(3):
    a.append(int(sys.stdin.readline().rstrip()))
    gop*=a[i]

b=list(str(gop))

for i in range(10):
    print(b.count(str(i)))

'''
b=list(str(gop))
곱한 값을 문자열로 바꿔
b에 리스트 형태로 담기

print(b.count(str(i)))
str(i)로 i를 문자로 바꿔주고
i=0일때 b리스트에 0의 개수 출력
'''

#3052
import sys
a=[]
b=[]
for i in range(10):
    a.append(int(sys.stdin.readline().rstrip()))
    b.append(a[i]%42)
b=set(b)
print(len(b))

'''
a배열에는 입력숫자 저장
b배열에는 42로 나눈 나머지 저장
리스트b를 세트로 바꿔
중복을 허용하지 않도록 바꾸고
len(b)로 b의 개수 출력
'''

#1546
import sys
n=int(sys.stdin.readline().rstrip())
a=list(map(int,sys.stdin.readline().split()))
max=max(a)
res=0
for i in range(n):
    a[i] = a[i]/max * 100
    res+=a[i]
print(res/n)

#8958
import sys
n=int(sys.stdin.readline().rstrip())

for i in range(n):
    a=list(sys.stdin.readline().rstrip())
    sum=0
    score=0
    for j in a:
        if j == "O":
            score+=1
            sum+=score
        else:
            score=0
    print(sum)

'''
a에 OOXXOXXOOO 입력받음
for j in OOXXOXXOOO
#8958번 다시풀기!
'''

#4344
import sys
c=int(sys.stdin.readline().rstrip())
for i in range(c):
    count=0
    a=list(map(int,sys.stdin.readline().split()))
    mid=sum(a[1:])/a[0] #평균
    for j in a[1:]:
        if (j > mid):
            count+=1
    print("%.3f" %(count/a[0]*100)+"%")

'''
for j in a:
이렇게 하면 안되고
for j in a[1:]으로 해야
a의 첫 번째 원소를 빼고
두 번째 원소부터 시
'''
