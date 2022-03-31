#2739
n = int(input())

for i in range(1,10):
    print(n, "*", i, "=", n*i)

#10950
t = int(input()) #test case 개수

for i in range(t):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)

'''
for a,b in range(t) 이렇게 하면 안됨
split() ==> 공백제거 외우기
'''

#8393
n = int(input())
sum=0

for i in range(n):
    a = n-i
    sum=sum+a
    
print(sum)

'''
for i in range(n)에서 i와 n이 무엇을 가리키는지
잘 생각해보기!
'''

#15552

'''
입출력 방식이 느리면 여러줄을 입력받거나
출력할 때 시간초과가 날 수 있다.

Python을 사용하고 있다면
input 대신 sys.stdin.readline을 사용할 수 있다.
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에
문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
'''
import sys
t = int(sys.stdin.readline())

for i in range(t):
    a,b = sys.stdin.readline().split()
    a=int(a)
    b=int(b)
    print(a+b)

#2741
import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(i)

#11021
import sys
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    a,b=sys.stdin.readline().split()
    a=int(a)
    b=int(b)
    print("Case #%d: %d" %(i+1,a+b))

  
'''
print("Case #",i+1,":",a+b)
으로 했을 때 잘 출력이 되지만
예제의 출력이랑은 다름

*구글링
print("Case #%d: %d" %(i+1,a+b))
%d %f %s %c를 이용하고, %()를 이용해서 변수 입력
'''

#11022
import sys
t=int(sys.stdin.readline().rstrip())

for i in range(t):
    a,b=sys.stdin.readline().split()
    a=int(a)
    b=int(b)
    print("Case #%d: %d + %d = %d" %(i+1, a, b, a+b))


#sys.stdin.readlind().split() 외우기!
