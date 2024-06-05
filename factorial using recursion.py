#1.

print("1. factorial using recursion")
def factorial(n):
    if n == 1 or 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number: "))
print(factorial(n))


# without recursion
"""n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)
"""