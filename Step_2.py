
#1330
a,b = input().split()
a = int(a)
b = int(b)

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")

#9498
score = int(input())
if (score >= 90):
    print("A")
elif (score >=80):
    print("B")
elif (score >= 70):
    print("C")
elif (score >= 60):
    print("D")
else:
    print("F")

#2753
year = int(input())
if(year%4==0)&(year%100!=0):  #if(year%4==0 & year%100!=0)로 하면 안됨
    print("1")
elif(year%400==0):
    print("1")
else:
    print("0")
    
#14681
a = int(input())
b = int(input())

if(a>0) & (b>0):
    print(1)
elif(a<0) & (b>0):
    print(2)    
elif(a<0) & (b<0):
    print(3)
else:
    print(4)

#2884
a,b = input().split()
a = int(a)
b = int(b) #a시 b분

'''
처음 코드 ---(1)
if(a==0):
    a=24

if(b>=45):
    print(a,b-45)
else:
    print(a-1,b+60-45)
'''

#바꾼 코드 ---(2)
if(a==0):
    if(b>=45):
        print(a,b-45)
    else:
        print(a-1+24,b+60-45)
else:
    if(b>=45):
        print(a,b-45)
    else:
        print(a-1,b+60-45)
'''
(1)로 했을 때 0 13을 입력하면 23 28로 출력되서 맞는 코드라고 생각했는데
이렇게 입력하면 0 50을 입력했을 때 24 50이라고 출력되므로 오류
'''

#2525
a,b = input().split()
a = int(a)
b = int(b) #현재시각 a시 b분

c = int(input()) #소요시간
min = b+c

'''
처음코드 ---(1)
if(min>=60):
    a=a+1
    min=min-60

if(a>=24):
    a=a-24
    if(min>=60):
        a=a+1
        min=min-60
'''
#바꾼 코드 ---(2)
if(min>=60):
    a=a+(min//60)
    min=min%60
      
if(a>=24):
    a=a-24
    if(min>=60):
        a=a+(min//60)
        min=min%60
        
print(a,min) #끝나는 시간

'''
(1)로 했을 때는 23시10분에 200분을 추가했을 때 1 90으로 출력된다.
그래서 몫과 나머지를 이용해야 한다고 생각을 했고
//60을 이용해서 몫만 시간에 더해주고
%60을 이용해서 나머지를 분에 넣어준다고 생각했다.
'''

#2480
a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

if(a==b==c):
    prize = 10000 + a*1000
elif(a==b):
    prize = 1000 + a*100
elif(a==c):
    prize = 1000 + a*100
elif(b==c):
    prize = 1000 + b*100
else:
    m=max(a,b,c)
    prize = m*100

print(prize)

'''
max(a,b,c)가 파이썬에서는 가능
다른 언어에서는 max(a,b)로 먼저 해주고 max(max(a,b),c) 이런 형식으로 해주어야 
'''
