# fibonacci Series for nth term from the user

n=int(input("enter the nth term of the series "))
a=0
s=0
i=2
b=1
print("Fibonacci series for first",n,"terms")
print(a)   # first value in the series
print(b)   # second value in the series
while i<n:
    s=a+b
    a=b
    b=s
    i+=1
    print(s)