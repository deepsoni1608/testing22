n = int(input("enter the limit for fibonaci"))
a, b = 0, 1
num = 0
if n<=0:
    print("enter positive number")

while num < n:
    print(a)
    c = a + b
    a = b
    b = c
    num=num+1

#with reccursion

def fib(n):
    if(n<0):
        print("invalid")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(9))






