Home work
def number():
    a = int(input('A sonni qiriting: '))
    b = int(input('B sonni qiriting: '))
    c = int(input('C sonni qiriting: '))
    a,c = c,a
    b,a = a,b
    c,b = c,b
    print(a,b,c)

# 2
def hisbokitob():
    n = int(input('sonni qiriting: '))
    n_1 = int(input('sonni qiriting: '))
    if n <0:
        print('-1')
    elif n >0:
        print('1')
    elif n == 0:
        print('0')
    print(n,'+',n_1,'=',n+n_1)
#
# 3
def Deskriminant()
a = int(input('sonni qiriting: '))
b = int(input('sonni qiriting: '))
c = int(input('sonni qiriting: '))
x = 1
z = a * (x**2)+b*x +c
if z >0:
    print(z)
elif z== 0:
    print(z)
else:
    print('ildiz yoq ')

# 4
def doira():
    n = int(input("Sonni qiriting: "))
    print((n**2)*3.1415)

def uchburchek():
    a = int(input('sonni qiriting: '))
    b = int(input('sonni qiriting: '))
    c = (a**2)+(b**2)
    p =a +b +c
    print(p)
# 5

def cal():
    a = int(input('sonni qiriting: '))
    b = int(input('sonni qiriting: '))
    c = int(input('sonni qiriting: '))
    if c == 1:
        print(a,'-',b,'=',a-b)
    elif c ==2:
        print(a,'*',b,'=',a*b)
