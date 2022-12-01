
# program to determine sum of all odd and even numbers for user defined n terms

n=int(input("Enter the nth value "))
a=0
b=0

for i  in range (1,n+1):
    if(i%2==0):
        #print (i,"is even")
        a+=i   

    else:
        #print(i,"is odd")
        b+=i 

print("The sum of all even numbers is ",a)
print("The sum of all odd numbers is ",b)       