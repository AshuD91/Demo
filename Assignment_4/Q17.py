# factorial of a number n
m=0
k=1
n=int(input("Enter any  number "))
if n==0:
    print("The factorial of zero is ",k)
else:    
    for i in range (1,n+1):
        m=i*k
        k=m
    print("Factorial of the given number",n," is ",m)