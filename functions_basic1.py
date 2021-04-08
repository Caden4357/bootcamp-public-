#1This will return 5
def a():
    return 5
print(a())
#2This will return 10
def a():
    return 5
print(a()+a())
#3This will return 5
def a():
    return 5
    return 10
print(a())
#4 This will return 5 
def a():
    return 5
    print(10)
print(a())
#5 This will print 5 and None
def a():
    print(5)
x = a()
print(x)
#6 This will print 3 and 5 with an error because the sum of b+c is not being stored anywhere
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#7 This is not adding two numbers but comibing 2 numbers together so this would return 25 very cool!
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#8 This will print 100 and return 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
        return 7
print(a())
#9 This will return 7, 14, 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
        return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#10 This will return 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#11 This will print 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#12 This will print 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#13 This will print 500, 500, 300, 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#14 This will print 1, 3, 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#15 This will print 1, 3, 5, 10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)









