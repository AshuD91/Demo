#Program to calculate the sum of digits

a=0
b=0
n=int(input("Enter the number "))

while n>0:
    a=n%10
    n=n//10
    b+=a
print("The sum of digits of entered number is ",b)