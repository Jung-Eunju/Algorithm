#2557
print("Hello World!")

#10718
print("강한친구 대한육군")
print("강한친구 대한육군")


#10171
print("\\    /\\")
print(" )  ( ')")      
print("(  /  )")
print(" \\(__)|")


# 역슬래시 \ 사용시
# 문자로 사용하려면 \앞에 \하나 더 붙여야 함

#10172
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")


# " or ' 이런거 쓸 때도
# 앞에 \하나 붙여야 함


#1000
a,b = input().split()
print(int(a)+int(b))

# 파이썬에서 입력을 받을 때는 input()사용
# 스페이스로 a,b가 나누어 지므로 split()으로 공백을 기준으로 나눔
# input()은 문자열로 저장되므로 int(a),int(b)로 정수형으로 바꿔주기

#1001
a,b=input().split()
print(int(a)-int(b))

#10998
a,b = input().split()
print(int(a)*int(b))

#1008
a,b = input().split()
print(int(a)/int(b))

#10869
a,b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))

#10926
a=input()
print(a+"??!")

#18108
a = int(input())
print(a-543)

#10430
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#2588
a=int(input())
b=int(input())
print(a*(b%10)) #1의자리
print(a*((b%100)//10)) #10의 자리
print(a*(b//100)) #100의 자리
print(a*b)
