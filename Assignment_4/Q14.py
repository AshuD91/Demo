# program to determine a given number is prime or not 

b= int(input("Enter the number "))
c=1
for n in range (2,b):
    if (b/2 % n==0):
        c=0
        break
if c==1:
    print(b," is a prime number")
else:
    print(b," is not a prime number")


