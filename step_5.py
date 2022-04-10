#15596 https://www.acmicpc.net/problem/15596
def solve(a):
    sum=0
    for i in a:
        sum+=i
    return sum

#4673 https://www.acmicpc.net/problem/2673 다시풀기!
'''
def d(n):
    print(n)
    a=n//10
    b=n%10
    n=n+a+b
    
    return d(n)

d(1)
'''

def d(n):
    n=n+sum(map(int,str(n)))
    return n

nonSelfNum = set()

for i in range(1,1001):
    nonSelfNum.add(d(i))

print(nonSelfNum)

for j in range(1,1001):
    if j not in nonSelfNum:
        print(j)


#1065 https://www.acmicpc.net/problem/1065 다시!
import sys
n=int(sys.stdin.readline().rstrip())


def han(n):
    count=0
    for i in range(1,n+1):
        num_list = list(map(int,str(i)))
        if i<100:
            count+=1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count+=1
    return count

print(han(n))
