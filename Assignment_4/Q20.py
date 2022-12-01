#program for getting multiplication table of two numbers as output

# a=int(input("enter the number" ))
# for x in range (2):
#     a+=x
#     print("multiplication table of ",a,"is")
#     for i in range (1,11):
#         c=a*i
#         print(a,"*",i,"=",c)


a=int(input("Enter the number " ))
b=int(input("Enter the number " ))

print("multiplication table of ",a,"is")

for i in range (1,11):
        c=a*i
        print(a,"*",i,"=",c)

print("multiplication table of",b,"is")

for j in range (1,11):
        d=b*j
        print(b,"*",j,"=",d)