#2438
import sys
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    print("*" * (i+1))

#2439
import sys
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    re=("*" * (i+1))
    print(re.rjust(n))
'''
ljust(전체자리수): 왼쪽정렬
rjust(전체자리수): 오른쪽정
'''

#10871
import sys
n,x = sys.stdin.readline().split()
n=int(n)
x=int(x)
a = []
b = []


a=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    if a[i] < x:
        print(a[i],end=" ")
        #b.append(a[i])
#print(b)

'''
a=list(map(int,sys.stdin.readline().split()))
배열로 입력받기! 이거 꼭 외우기!!

a를 n개 입력받아야 한다고 해서 for문 안에 넣었었는데
그냥 바깥에서 입력받아야 됨

a,b배열을 만들어 a[i] < x 인것을 b배열에 추가하여
b배열을 print()하는 방식으로 하려고 하였으나
오류가 남
그래서 그냥 print()를 하고
end=" "로 줄바꿈이 안일어나도록 하였다.

n,x를 받을 때도 이제는 n,x=map(int,sys.stdin.readlin().split())으로 받기!
'''

#10952
import sys
while True:
    a,b = sys.stdin.readline().rsplit()
    a=int(a)
    b=int(b)
    if a==0 & b==0:
        break
    print(a+b)
   
   
'''
테스트케이스의 수가 정해져있지 않기 때문에
for문 사용하지 않고 while True문 사용
'''

#10951
import sys
while True:
    try:
        a,b = sys.stdin.readline().rsplit()
        a=int(a)
        b=int(b)
        print(a+b)
    except:
        break
     
'''
try-except문을 사용해서 풀기!
'''

#1110
import sys
n = int(sys.stdin.readline()) #26
old=n

count=0

while True:
    a=n//10
    b=n%10
    new=(10*b)+((a+b)%10) #새로운 숫자 68
    count=count+1
    n=new
    if old==new:
        break
    
print(count)


'''
n 숫자 입력 ==> old변수에 숫자 저장

new변수에 새로운 숫자 저장

count횟수 증가

n변수를 new와 같다고 해서
while True문이 계속 돌아가도록 하고

첫 입력숫자인 old와 바뀌는 숫자 new가
같으면 break
'''
#복습 필수! 어려웠음...
    

