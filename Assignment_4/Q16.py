# fibonacci series upto first n terms say n=10

n=10
a=0
s=0
i=2
b=1
print("Fibonacci series for first 10 terms")
print(a)   # first value in the series
print(b)   # second value in the series
while i<n:
    s=a+b
    a=b
    b=s
    i+=1
    print(s)